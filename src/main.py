import time

from train import image_to_label_ner, predict_step, image_to_label_keywords


def main():
    print(predict_step(["./data/raw/kucing.jpg"]))
    print(image_to_label_ner(["./data/raw/kucing.jpg"]))
    print(image_to_label_keywords(["./data/raw/kucing.jpg"], ["cat", "dog"]))

    # Diberi pilihan, mau based on keyword atau NER


if __name__ == "__main__":
    main()
