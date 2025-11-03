import numpy as np
import cv2

from src.functions.ellipse_params import calculate_center_of_image, calculate_axes_size_from_image_size
from src.utils.cell_settings import border_line_thickness
from src.utils.classes.cancer_nucleus import CancerNucleus


def single_cell_generator_with_open_window(size_x: int, size_y: int):
    """
    Generates a single cell-like image with a nucleus, displays the created image in
    an open window, and waits for the user's input to close.

    This function first creates a blank image of the given size with three color
    channels. It then initializes a CancerNucleus instance with parameters like the
    center, axes, angle, irregularity, and border thickness calculated based on the
    provided image size. The nucleus is drawn on the image, and the resulting image
    is displayed in a new window.

    Args:
        size_x (int): Width of the generated image.
        size_y (int): Height of the generated image.

    """
    image = np.zeros((size_x, size_y, 3), dtype=np.uint8)
    cancer_nucleus = CancerNucleus(center=calculate_center_of_image(size_x, size_y),
                                   axes=calculate_axes_size_from_image_size(size_x, size_y),
                                   angle=np.random.randint(0, 360),
                                   irregularity=0.2,
                                   border_thickness=border_line_thickness(size_x, size_y))

    cancer_nucleus.draw_nuclei(image)
    cv2.imshow('Nucleus',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def single_cell_generator_with_return_image(size_x: int, size_y: int):
    """
    Generate an image of a single cell with its nucleus.

    This function creates a single cell with a nucleus represented in an image of specified size.
    The size and characteristics of the nucleus are determined based on the image dimensions
    and various random and calculated parameters.

    Args:
        size_x (int): The width of the image in pixels.
        size_y (int): The height of the image in pixels.

    Returns:
        np.ndarray: A 3D NumPy array representing the image with a single cell nucleus, where
                    the shape of the array is (size_x, size_y, 3) and dtype is uint8.
    """
    image = np.zeros((size_x, size_y, 3), dtype=np.uint8)
    cancer_nucleus = CancerNucleus(center=calculate_center_of_image(size_x, size_y),
                                   axes=calculate_axes_size_from_image_size(size_x, size_y),
                                   angle=np.random.randint(0, 360),
                                   irregularity=0.2,
                                   border_thickness=border_line_thickness(size_x, size_y))

    cancer_nucleus.draw_nuclei(image)
    return image



