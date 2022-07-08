import glob
import time

from train import image_to_label_ner, image_to_label_keywords


def main(mode="keywords"):

    cat_images_path = []
    dog_images_path = []
    for file in glob.glob("data\\raw\\cat\\*.jpeg"):
        cat_images_path.append(file)

    for file in glob.glob("data\\raw\\dog\\*.jpeg"):
        dog_images_path.append(file)

    cat_label = []
    dog_label = []

    if mode == "keywords":
        print("== Keywords mode ==")
        print(f"Starting to predict 🐱 with {len(cat_images_path)} images...")
        cat_start_time = time.time()
        for file in cat_images_path:
            cat_label.append(image_to_label_keywords([file], ["cat"]))
        print("Done predicting 🐱 in {} seconds".format(
            time.time() - cat_start_time))

        print(f"Starting to predict 🐶 with {len(dog_images_path)} images...")
        dog_start_time = time.time()
        for file in dog_images_path:
            dog_label.append(image_to_label_keywords([file], ["dog"]))
        print("Done predicting 🐶 in {} seconds".format(
            time.time() - dog_start_time))

        true_cat_pred = [cat for cat in cat_label if cat == "cat"]
        true_dog_pred = [dog for dog in dog_label if dog == "dog"]

        print(
            f"Cat true prediction accuracy : {len(true_cat_pred) / len(cat_label) * 100}%")
        print(
            f"Dog true prediction accuracy : {len(true_dog_pred) / len(dog_label) * 100}%")

        """
        Done predicting 🐱 in 14.83539342880249 seconds
        Cat true prediction accuracy : 94.5945945945946%

        Done predicting 🐶 in 10.83300232887268 seconds
        Dog true prediction accuracy : 94.87179487179486%
        """
    elif mode == "NER":
        print("== NER mode ==")
        print(f"Starting to predict 🐱 with {len(cat_images_path)} images...")
        cat_start_time = time.time()
        for file in cat_images_path:
            cat_label.append(image_to_label_ner([file]))
        print("Done predicting 🐱 in {} seconds".format(
            time.time() - cat_start_time))

        print(f"Starting to predict 🐶 with {len(dog_images_path)} images...")
        dog_start_time = time.time()
        for file in dog_images_path:
            dog_label.append(image_to_label_ner([file]))
        print("Done predicting 🐶 in {} seconds".format(
            time.time() - dog_start_time))

        true_cat_pred = [cat for cat in cat_label if cat == "cat"]
        true_dog_pred = [dog for dog in dog_label if dog == "dog"]

        print(
            f"Cat true prediction accuracy : {len(true_cat_pred) / len(cat_label) * 100}%")
        print(
            f"Dog true prediction accuracy : {len(true_dog_pred) / len(dog_label) * 100}%")
        """
        Done predicting 🐱 in 27.089590311050415 seconds
        Cat true prediction accuracy : 78.37837837837837%

        Done predicting 🐶 in 23.333070039749146 seconds
        Dog true prediction accuracy : 84.61538461538461%
        """

if __name__ == "__main__":
    main(mode="NER")
