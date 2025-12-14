import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras import layers
from tensorflow.keras.models import Model

from src.data_generation.data_generator import set_generator


def load_data():
    (x_train)  = set_generator(5000)
    (x_test) = set_generator(1000)
    x_train = np.array(x_train, dtype='float32') / 255.
    x_test = np.array(x_test, dtype='float32') / 255.

    return x_train, x_test