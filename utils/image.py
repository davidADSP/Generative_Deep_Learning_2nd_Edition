
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

def preprocess(imgs):
    """
    Normalize and reshape the images
    """
    imgs = imgs.astype("float32") / 255.0
    imgs = np.pad(imgs , ((0,0), (2,2), (2,2)), constant_values= 0.0)
    imgs = np.expand_dims(imgs, -1)
    return imgs



def noise(imgs, noise_factor):
    """
    Adds random noise to each image in the supplied array.
    """
    noisy_img = imgs + noise_factor * np.random.normal(
        mean=0.0, stddev=1.0, shape=np.shape(imgs)
    )

    return np.clip_by_value(noisy_img, 0.0, 1.0)



def display(images, n = 10, size = (20,3), cmap = 'Greys', as_type = 'float32', save_to = None):
    """
    Displays n random images from each one of the supplied arrays.
    """
    plt.figure(figsize=size)
    for i in range(n):
        ax = plt.subplot(1, n, i + 1)
        plt.imshow(images[i].astype(as_type), cmap=cmap)
        plt.axis("off")
    
    if save_to:
        out = plt.savefig(save_to)
        print(f'\nSaved to {save_to}')

    plt.show()
        