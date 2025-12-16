from data_generation.picture_generator import generate_image_with_random_aligment
from src.data_generation.single_cell_generator import calculate_axes_size_from_image_size, single_cell_generator_with_return_image
import numpy as np


def set_generator(num_pictures : int, size_x : int = 28, size_y : int = 28):
    """
    Generates a list of pictures by calling a single cell image generator function multiple times.

    This function creates a specified number of single cell images with a predefined width and
    height. It returns a list containing the generated images.

    Args:
        num_pictures (int): Number of pictures to generate.
        size_x (int): Width of each image in pixels. Defaults to 28.
        size_y (int): Height of each image in pixels. Defaults to 28.

    Returns:
        list: A list of generated images.
    """
    list_of_pictures = []

    for _ in range(num_pictures):
        image = single_cell_generator_with_return_image(size_x, size_y)
        list_of_pictures.append(image)

    return list_of_pictures


def set_generator_with_random_aligment(num_pictures : int, size_x : int = 128, size_y : int = 128):

    list_of_pictures = []

    for _ in range(num_pictures):
        image = proba_losowego = generate_image_with_random_aligment()
        list_of_pictures.append(image)

    return list_of_pictures