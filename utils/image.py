
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

def preprocess(img):
    """
    Normalizes the supplied array and reshapes it into the appropriate format.
    """
    img = img / 255.0
    return img

def noise(img, noise_factor):
    """
    Adds random noise to each image in the supplied array.
    """
    noisy_img = img + noise_factor * tf.random.normal(
        mean=0.0, stddev=1.0, shape=tf.shape(img)
    )

    return tf.clip_by_value(noisy_img, 0.0, 1.0)


def sample_batch(dataset):
    return dataset.take(1).get_single_element().numpy()



def display(images, n = 9, size = (20,3), cmap = 'Greys', as_type = 'float32'):
    """
    Displays n random images from each one of the supplied arrays.
    """
    plt.figure(figsize=size)
    for i in range(n):
        ax = plt.subplot(1, n, i + 1)
        plt.imshow(images[i].astype(as_type), cmap=cmap)
        plt.axis("off")