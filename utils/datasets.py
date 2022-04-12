import numpy as np


def sample_batches(dataset, batches):
    return np.concatenate(list(dataset.take(batches)))


def sample_batch(dataset):
    return dataset.take(1).get_single_element().numpy()
