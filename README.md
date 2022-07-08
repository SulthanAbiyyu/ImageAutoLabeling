# Image Auto Labeling

This project based on captioning [model](https://huggingface.co/nlpconnect/vit-gpt2-image-captioning) and NER model.

## TODO

- [x] Make dataset scraping script
- [x] Make bulk image labeling logic
- [x] Add evaluation

**Paradox that asked by my friend**: If one could auto label, then why need to train another model?

To answer the paradox, imagine you have a lot of random image data. You want to use the image to train other models. Because the data is random, you need to select it manually. In order to solve the problem, I try to utilize captioning + NER / keyword based model.