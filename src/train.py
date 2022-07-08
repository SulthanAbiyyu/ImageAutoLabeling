import torch
import pickle

from PIL import Image

model = pickle.load(open(
    "pickle/model.pkl", "rb"))
feature_extractor = pickle.load(open("pickle/feature_extractor.pkl", "rb"))
tokenizer = pickle.load(open("pickle/tokenizer.pkl", "rb"))

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)


max_length = 16
num_beams = 4
gen_kwargs = {"max_length": max_length, "num_beams": num_beams}


def predict_step(image_paths):
    images = []
    for image_path in image_paths:
        i_image = Image.open(image_path)
        if i_image.mode != "RGB":
            i_image = i_image.convert(mode="RGB")

        images.append(i_image)

    pixel_values = feature_extractor(
        images=images, return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)

    output_ids = model.generate(pixel_values, **gen_kwargs)

    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]
    return preds


def image_to_label_ner(image_paths):
    nlp = pickle.load(open("pickle/nlp.pkl", "rb"))
    preds = predict_step(image_paths)

    text = nlp(preds[0])
    for token in text:
        # if(token.dep_ == "nsubj"):
        #     return token.text
        # if token.tag_ == "NNP":
        #     return token.text
        if (token.dep_ == "ROOT"):
            return token.text


def image_to_label_keywords(image_paths: str, keywords: list) -> str:
    preds = predict_step(image_paths)[0]

    for keyword in keywords:
        if keyword in preds:
            return keyword
        else:
            return "None"
