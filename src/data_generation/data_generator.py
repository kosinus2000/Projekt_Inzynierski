import numpy as np
import cv2
import matplotlib.pyplot as plt


def random_dimension_generator():

    """
    Generates a random dimension for an image.
    The dimension is a tuple of (height, width) where both height and width are between 100 and 1000.
    """
    height = np.random.randint(100, 1001)
    width = np.random.randint(100, 1001)
    return (height, width)