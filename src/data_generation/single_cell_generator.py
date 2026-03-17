import numpy as np
import cv2
import matplotlib.pyplot as plt
from src.functions.ellipse_params import calculate_center_of_image, calculate_axes_size_from_image_size
from src.utils.cell_settings import border_line_thickness, generate_color_variation_normal
from src.utils.classes.cancer_nucleus import CancerNucleusOld


def single_cell_generator_with_open_window(size_x: int, size_y: int, random_colors: bool = False):
    """
    Generates a single cell-like image with a nucleus, displays the created image in
    an open window, and waits for the user's input to close.

    This function first creates a blank image of the given size with three color
    channels. It then initializes a CancerNucleusOld instance with parameters like the
    center, axes, angle, irregularity, and border thickness calculated based on the
    provided image size. The nucleus is drawn on the image, and the resulting image
    is displayed in a new window.

    Args:
        size_x (int): Width of the generated image.
        size_y (int): Height of the generated image.
        random_colors (bool): If True, generates random color variations for the nucleus.

    """
    image = np.zeros((size_x, size_y, 3), dtype=np.uint8)

    base_color = (160, 83, 179)
    border_color = (107, 26, 121)

    if random_colors:
        base_color = generate_color_variation_normal(base_color)
        border_color = generate_color_variation_normal(border_color)

    cancer_nucleus = CancerNucleusOld(center=calculate_center_of_image(size_x, size_y),
                                      axes=calculate_axes_size_from_image_size(size_x, size_y),
                                      angle=np.random.randint(0, 360),
                                      irregularity=0.2,
                                      color=base_color,
                                      border_color=border_color,
                                      border_thickness=border_line_thickness(size_x, size_y))

    cancer_nucleus.draw_nuclei(image)
    plt.imshow(image)
    plt.axis('off')  # usuwa osie
    plt.show()


def single_cell_generator_with_return_image(size_x: int, size_y: int, random_colors: bool = False):
    """
    Generate an image of a single cell with its nucleus.

    This function creates a single cell with a nucleus represented in an image of specified size.
    The size and characteristics of the nucleus are determined based on the image dimensions
    and various random and calculated parameters.

    Args:
        size_x (int): The width of the image in pixels.
        size_y (int): The height of the image in pixels.
        random_colors (bool): If True, generates random color variations for the nucleus.

    Returns:
        np.ndarray: A 3D NumPy array representing the image with a single cell nucleus, where
                    the shape of the array is (size_x, size_y, 3) and dtype is uint8.
    """
    image = np.zeros((size_x, size_y, 3), dtype=np.uint8)

    base_color = (160, 83, 179)
    border_color = (107, 26, 121)

    if random_colors:
        base_color = generate_color_variation_normal(base_color)
        border_color = generate_color_variation_normal(border_color)

    cancer_nucleus = CancerNucleusOld(center=calculate_center_of_image(size_x, size_y),
                                      axes=calculate_axes_size_from_image_size(size_x, size_y),
                                      angle=np.random.randint(0, 360),
                                      irregularity=0.2,
                                      color=base_color,
                                      border_color=border_color,
                                      border_thickness=border_line_thickness(size_x, size_y))

    cancer_nucleus.draw_nuclei(image)
    return image



