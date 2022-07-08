from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import urllib.request
import base64
import time
import os


def scrape_images(objects: dict, DRIVER_PATH: str, OUTPUT_PATH: str, LIMIT: int):
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    for object, img_link in objects.items():

        driver = webdriver.Chrome(DRIVER_PATH, chrome_options=chrome_options)
        driver.get(img_link)

        if not os.path.exists(OUTPUT_PATH + f"/{object}"):
            os.makedirs(OUTPUT_PATH + f"/{object}")

        while True:
            last_height = driver.execute_script(
                "return document.body.scrollHeight")
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = driver.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        image_elements = driver.find_elements_by_class_name('rg_i')
        if len(image_elements) > LIMIT:
            image_elements = image_elements[:LIMIT]

        counter = 0
        for image in image_elements:

            if (image.get_attribute('src') is not None):
                my_image = image.get_attribute(
                    'src').split('data:image/jpeg;base64,')
                filename = OUTPUT_PATH + \
                    f"/{object}/" + object + str(counter)+'.jpeg'

                if(len(my_image) > 1):
                    with open(filename, 'wb') as f:
                        f.write(base64.b64decode(my_image[1]))
                else:
                    print(image.get_attribute('src'))
                    urllib.request.urlretrieve(image.get_attribute(
                        'src'), OUTPUT_PATH + f"/{object}/" + object + str(counter)+'.jpeg')
                counter += 1

        driver.quit()


if __name__ == "__main__":
    DRIVER_PATH = "src\chromedriver.exe"
    OUTPUT_PATH = "data/raw"
    LIMIT = 50
    objects = {
        "cat": "https://www.google.com/search?q=cat&rlz=1C1MSIM_enID949ID949&sxsrf=ALiCzsbgBI8puYQertsnqzxCVYSFLz7L7w:1657277641169&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiq_-GokOn4AhWBm9gFHQR-C1YQ_AUoAXoECAMQAw&biw=1920&bih=947&dpr=1",
        "dog": "https://www.google.com/search?q=dog&rlz=1C1MSIM_enID949ID949&sxsrf=ALiCzsai2Vi2E7oTLhekk6ntCNS9-S6skw:1657278125403&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiTodWPkun4AhV763MBHdMJCVEQ_AUoAXoECAMQAw&biw=1920&bih=890&dpr=1"
    }
    scrape_images(objects, DRIVER_PATH, OUTPUT_PATH, LIMIT)
