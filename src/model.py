import pickle
import spacy
from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer

model = VisionEncoderDecoderModel.from_pretrained(
    "nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTFeatureExtractor.from_pretrained(
    "nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained(
    "nlpconnect/vit-gpt2-image-captioning")
nlp = spacy.load("en_core_web_sm")

with open("pickle/model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("pickle/tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)

with open("pickle/feature_extractor.pkl", "wb") as f:
    pickle.dump(feature_extractor, f)

with open("pickle/nlp.pkl", "wb") as f:
    pickle.dump(nlp, f)
