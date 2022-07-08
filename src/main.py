import glob
import time

import pandas as pd

from train import image_to_label_ner, image_to_label_keywords


def main():
    # print(predict_step(["./data/raw/kucing.jpg"]))
    # print(image_to_label_ner(["./data/raw/kucing.jpg"]))
    # print(image_to_label_keywords(["./data/raw/kucing.jpg"], ["cat", "dog"]))

    # Diberi pilihan, mau based on keyword atau NER

    # Test keyword based prediction
    cat_images_path = []
    dog_images_path = []
    for file in glob.glob("data\\raw\\cat\\*.jpeg"):
        cat_images_path.append(file)

    for file in glob.glob("data\\raw\\dog\\*.jpeg"):
        dog_images_path.append(file)

    print(f"Starting to predict 🐱 with {len(cat_images_path)} images...")
    cat_start_time = time.time()
    cat_label = image_to_label_keywords(cat_images_path, ["cat"])
    print("Done predicting 🐱 in {} seconds".format(time.time() - cat_start_time))

    print(f"Starting to predict 🐶 with {len(dog_images_path)} images...")
    dog_start_time = time.time()
    dog_label = image_to_label_keywords(dog_images_path, ["dog"])
    print("Done predicting 🐶 in {} seconds".format(time.time() - dog_start_time))

    print(
        f"Cat unique label results : {pd.DataFrame(cat_label).value_counts()}")
    print(
        f"Dog unique label results : {pd.DataFrame(dog_label).value_counts()}")


if __name__ == "__main__":
    main()
