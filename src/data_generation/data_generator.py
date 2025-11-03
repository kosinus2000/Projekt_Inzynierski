from src.data_generation.single_cell_generator import calculate_axes_size_from_image_size, single_cell_generator_with_return_image
import numpy as np


def set_generator(num_pictures : int):
    """
    Generates a list of images using the `single_cell_generator_with_return_image` function. The
    generated images have dimensions of 28x28 pixels and the total number of images returned
    is determined by the `num_pictures` parameter.

    Args:
        num_pictures (int): The number of pictures to generate.

    Returns:
        list: A list containing the generated images.
    """
    list_of_pictures = []

    for _ in range(100):
        image = single_cell_generator_with_return_image(28, 28)
        list_of_pictures.append(image)

    return list_of_pictures