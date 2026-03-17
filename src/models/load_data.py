import numpy as np

from data_generation.data_generator import set_generator_with_random_aligment


def load_data(obj):
    (x_train)  = obj
    (x_test) = obj
    x_train = np.array(x_train, dtype='float32') / 255.
    x_test = np.array(x_test, dtype='float32') / 255.

    return x_train, x_test