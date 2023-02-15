import numpy as np


def sample_batches(dataset, batches):
    return np.concatenate(list(dataset.take(batches)))


def sample_batch(dataset):
    batch = dataset.take(1).get_single_element()
    if isinstance(batch, tuple):
        batch = batch[0]
    return batch.numpy()
