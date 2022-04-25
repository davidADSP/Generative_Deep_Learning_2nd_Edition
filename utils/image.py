
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


def display(images, n = 10, size = (20,3), cmap = 'gray_r', as_type = 'float32', save_to = None):
    """
    Displays n random images from each one of the supplied arrays.
    """
    if images.max() > 1.0:
        images = images / 255.0
    elif images.min() < 0.0:
        images = (images + 1.0) / 2.0

    plt.figure(figsize=size)
    for i in range(n):
        ax = plt.subplot(1, n, i + 1)
        plt.imshow(images[i].astype(as_type), cmap=cmap)
        plt.axis("off")
    
    if save_to:
        out = plt.savefig(save_to)
        print(f'\nSaved to {save_to}')

    plt.show()
        