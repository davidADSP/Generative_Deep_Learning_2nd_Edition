# 🦜 Generative Deep Learning - 2nd Edition Codebase

The official code repository for the second edition of the O'Reilly book *Generative Deep Learning: Teaching Machines to Paint, Write, Compose and Play*.

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

Many of the examples in this book are adapted from the excellent open source implementations that are available through the Keras website (https://keras.io/examples/generative/). I highly recommend you check out this resource as new models and examples are constantly being added.

## 🚀 Getting Started

### Kaggle API

To download some of the datasets for the book, you will need a Kaggle account and an API token. To use the Kaggle API:

1. Sign up for a Kaggle account at https://www.kaggle.com.
2. Go to the 'Account' tab of your user profile (https://www.kaggle.com/<username>/account)
3. Select 'Create API Token'. This will trigger the download of `kaggle.json`, a file containing your API credentials.

### The .env file

Create a file called `.env` in the root directory, containing the following values (replacing the Kaggle username and API key with the values from the JSON):

```
JUPYTER_PORT=8888
TENSORBOARD_PORT=6006
KAGGLE_USERNAME=<your_kaggle_username>
KAGGLE_KEY=<your_kaggle_key>
```

### Get set up with Docker

This codebase is designed to be run with Docker.

Don't worry if you've never used Docker before! To get set up, follow the instructions in the [Docker README](./docs/docker.md) file in this repository. This includes a full run through of why Docker is awesome and a description of how interact with the codebase using Docker.

### Building the Docker image

If you do not have a GPU, run the following command:

```
docker-compose build
```

If you do have a GPU that you wish to use, run the following command:

```
docker-compose -f docker-compose-gpu.yml build
```

## 🏃‍♀️ Running the Examples

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

The codebase comes with an in-built data downloader helper script.
Use the helper script as follows (from outside the container):

```
bash scripts/download.sh [faces, bricks, recipes, flowers, wines, cellosuites, chorales]
```

### Tensorboard

Tensorboard is really useful for monitoring experiments and seeing how your generative deep learning model training is progressing.

To launch Tensorboard, run the following script (from outside the container), replacing `<CHAPTER>` with the required chapter (e.g. `03_vae`) and `<EXAMPLE>` with the required example (e.g. `02_vae_fashion`).

```
bash scripts/tensorboard.sh <CHAPTER> <EXAMPLE>
```

Tensorboard will be available in your local browser on the port specified in your `.env` file - for example:
```
http://localhost:6006
```

### Using a cloud virtual machine

To set up a virtual machine with GPU in Google Cloud Platform, follow the instructions in the [Google Cloud README](./docs/googlecloud.md) file in this repository.



