import glob
import time

import pandas as pd

from train import image_to_label_ner, image_to_label_keywords


def main():
    # print(predict_step(["./data/raw/kucing.jpg"]))
    # print(image_to_label_ner(["./data/raw/kucing.jpg"]))
    # print(image_to_label_keywords(["./data/raw/kucing.jpg"], ["cat", "dog"]))

    # Test keyword based prediction
    cat_images_path = []
    dog_images_path = []
    for file in glob.glob("data\\raw\\cat\\*.jpeg"):
        cat_images_path.append(file)

    for file in glob.glob("data\\raw\\dog\\*.jpeg"):
        dog_images_path.append(file)

    cat_label = []
    dog_label = []

    print(f"Starting to predict 🐱 with {len(cat_images_path)} images...")
    cat_start_time = time.time()
    for file in cat_images_path:
        cat_label.append(image_to_label_keywords([file], ["cat"]))
    print("Done predicting 🐱 in {} seconds".format(time.time() - cat_start_time))

    print(f"Starting to predict 🐶 with {len(dog_images_path)} images...")
    dog_start_time = time.time()
    for file in dog_images_path:
        dog_label.append(image_to_label_keywords([file], ["dog"]))
    print("Done predicting 🐶 in {} seconds".format(time.time() - dog_start_time))

    true_cat_pred = [cat for cat in cat_label if cat == "cat"]
    true_dog_pred = [dog for dog in dog_label if dog == "dog"]

    print(
        f"Cat true prediction accuracy : {len(true_cat_pred) / len(cat_label) * 100}%")
    print(
        f"Dog true prediction accuracy : {len(true_dog_pred) / len(dog_label) * 100}%")

    """
    Cat true prediction accuracy : 94.5945945945946%
    Dog true prediction accuracy : 94.87179487179486%
    """


if __name__ == "__main__":
    main()
