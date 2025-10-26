import numpy as np
import cv2
import math

from src.functions.ellipse import CalculateCenterOfImage, CalculateAxesSizeFromImageSize, BorderLineThickness
from src.utils.cancer_nucleus import CancerNucleus


def single_cell_generator_with_open_window(size_x=int, size_y=int):
    """
    Generates a single cell image with a cancer nucleus and displays it in an open window.

    This function creates an image of specified dimensions and generates a cancer nucleus
    with specific properties including position, size, angle, irregularity, and border
    thickness. The nucleus is drawn on the image, and the image is displayed in a window.

    Args:
        size_x: Width of the generated image.
        size_y: Height of the generated image.
    """
    image = np.zeros((size_x, size_y, 3), dtype=np.uint8)
    cancer_nucleus = CancerNucleus( center=CalculateCenterOfImage(size_x, size_y),
                                    axes=CalculateAxesSizeFromImageSize(size_x, size_y),
                                    angle=np.random.randint(0, 360),
                                    irregularity=0.2,
                                    border_thickness=BorderLineThickness(size_x, size_y))

    cancer_nucleus.draw_nuclei(image)
    cv2.imshow('Nucleus',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def single_cell_generator_with_return_image(size_x=int, size_y=int):
    """
    Generates an image with a single cancer nucleus for simulation purposes.

    This function creates an image of specified dimensions with a black
    background and simulates a single cancer nucleus in it. The cancer
    nucleus properties, such as center, axes size, angle, irregularity,
    and border thickness, are calculated or randomized based on the
    image size.

    Args:
        size_x: The width of the generated image in pixels.
        size_y: The height of the generated image in pixels.

    Returns:
        numpy.ndarray: An image array representing the generated image
        with a single cancer nucleus.
    """
    image = np.zeros((size_x, size_y, 3), dtype=np.uint8)
    cancer_nucleus = CancerNucleus(center=CalculateCenterOfImage(size_x, size_y),
                                   axes=CalculateAxesSizeFromImageSize(size_x, size_y),
                                   angle=np.random.randint(0, 360),
                                   irregularity=0.2,
                                   border_thickness=BorderLineThickness(size_x, size_y))

    cancer_nucleus.draw_nuclei(image)
    return image