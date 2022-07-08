# Image Auto Labeling

## Background
ImageAutoLabeling is effective for tackling random image dataset-related tasks. For example, we have a lot of random images and want to take advantage of the dataset for training another model. Instead of manually selecting the images needed, we can utilize ImageAutoLabeling.

The intuition is to immitate how human think if human have to do similiar task. When human look to a random image, human will unconsciously describing the image. Then, human will be decide what will the image classified as by a certain subjective threshold.

To describe the image, we use [captioning model](https://huggingface.co/nlpconnect/vit-gpt2-image-captioning). Then, pick the wanted word for label via NER or keyword.
## Evaluation Results

The amount of images used for evaluation is considerably low due to the expensive computational cost.

### Keywords based model

| dataset | size      | time    | accuracy |
| ------- | --------- | ------- | -------- |
| Cat 🐱  | 37 images | 14.83 s | 94.6 %   |
| Dog 🐶  | 39 images | 10.83 s | 94.87 %  |

### NER based model

| dataset | size      | time    | accuracy |
| ------- | --------- | ------- | -------- |
| Cat 🐱  | 37 images | 27.08 s | 78.37 %  |
| Dog 🐶  | 39 images | 23.33 s | 84.61 %  |

For cases that we already know what image that we need, keyword based model have better accuracy and faster than NER based model. But NER model have a lot of potential cases that we might need. For example if we need to group similiar image in random image dataset.

### Limitations

Our biggest limitation is the expensive computational cost. This limits our chance to evaluate this method further. Than, if we use NER based model, it will depends on how the captioning model construct the sentence. Because basically NER model is parsing the token dependancy and looking for ROOT.