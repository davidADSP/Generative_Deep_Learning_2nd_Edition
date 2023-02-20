# 🦜 Generative Deep Learning: Official Codebase

The official code repository for the second edition of the O'Reilly book 'Generative Deep Learning: Teaching Machines to Paint, Write, Compose and Play'

https://learning.oreilly.com/library/view/generative-deep-learning/9781492041931/
https://www.amazon.com/Generative-Deep-Learning-Teaching-Machines/dp/1492041947/ref=sr_1_1

<img src="assets/book_cover.png" width="300px">

## 📖 Book Chapters

Below is a outline of the book chapters, with links to relevant notebook folders in the codebase.

Part I: Introduction to Generative Deep Learning

1. Generative Modeling
2. [Deep Learning](./notebooks/02_deeplearning/)

Part II: Methods

3. [Variational Autoencoders](./notebooks/03_vae/)
4. [Generative Adversarial Networks](./notebooks/04_gan/)
5. [Autoregressive Models](./notebooks/05_autoregressive/)
6. [Normalizing Flows](./notebooks/06_normflow/)
7. [Energy-Based Models](./notebooks/07_ebm/)
8. [Diffusion Models](./notebooks/08_diffusion/)

Part III: Applications

9. [Transformers](./notebooks/09_transformer/)
10. Advanced GANs
11. [Music Generation](./notebooks/11_music/)
12. World Models
13. Multimodal Models
14. Conclusion

The subfolders in the `notebooks` folder correspond to the chapters from the book.
Within each chapter, there are several examples of models that are again separated into different folders

## 🚀 Getting Started

### Kaggle API

To download some of the datasets for the book, you will need a Kaggle account and an API token

Follow the instructions here:
```
https://github.com/Kaggle/kaggle-api
```

Download the JSON file that stores your username and API key.

### The .env file

Create a file called `.env` in the root directory, containing the following values (replacing the Kaggle username and API key with the values from the JSON):

```
JUPYTER_PORT=8888
TENSORBOARD_PORT=6006
KAGGLE_USERNAME=<your_kaggle_username>
KAGGLE_KEY=<your_kaggle_key>
```

## 🏃‍♀️ Running the Examples

### Get set up with Docker

To get set up with Docker, follow the instructions in the [docker.md] file in this repository.

### Building the Docker image

If you do not have a GPU, run the following command:

```
docker-compose build
```

If you do have a GPU that you wish to use, run the following command:

```
docker-compose -f docker-compose-gpu.yml build
```

### Running the container

If you do not have a GPU, run the following command:

```
docker-compose up
```

If you do have a GPU that you wish to use, run the following command:

```
docker-compose -f docker-compose-gpu.yml up
```

The running notebooks will be available in your local browser, on the port specified in your env file - for example

```
http://localhost:8888
```

### Downloading data

The codebase comes with an in-built data downloader helper script. Use the script as follows:

```
bash scripts/download.sh [faces, bricks, recipes, flowers, wines, cellosuites, chorales]
```

### Tensorboard

To launch Tensorboard, run the following script, replacing `<CHAPTER>` with the required chapter (e.g. `03_vae`) and `<EXAMPLE>` with the required example (e.g. `02_vae_fashion`).

```
bash scripts/tensorboard.sh <CHAPTER> <EXAMPLE>
```

Tensorboard will be available in your local browser on the port specified in your `.env` file - for example:
```
http://localhost:6006
```

### Using a cloud virtual machine

To get set up with Google Cloud Platform, follow the instructions in the [googlecloud.md] file in this repository.



