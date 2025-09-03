import random
import cv2
import numpy as np

from src.functions.ellipse import ellipse_proportion, cell_size, cell_size_proportionally
from src.utils.cancer_nucleus import CancerNucleus
from src.utils.poisson_sampling import poisson_sampling


def generate_picture(width = 500, height = 500, proportionally = False ):
    """
    Generates an image based on a given width, height, and whether proportions should be
    maintained. The function applies Poisson sampling to generate points and draws cancer
    nucleus shapes within an image based on specified configurations.

    Args:
        width (int): The width of the generated image.
        height (int): The height of the generated image.
        proportionally (bool): Determines if the cell size should be calculated proportionally
            to the dimensions of the image.

    Returns:
        numpy.ndarray: An image represented as an array with the specified dimensions and
        generated decor.
    """

    points = poisson_sampling(width, height, 10)
    image = np.zeros((width, height, 3), np.uint8)



    for center_point in points:
        if proportionally:
            nuclei_size = cell_size_proportionally(width, height)
        else:
            nuclei_size = cell_size()
        axes = ellipse_proportion(nuclei_size)
        angle = random.randint(0, 360)

        (CancerNucleus(center=center_point,
                      axes= axes,
                      angle = angle,
                      thickness = -1,
                      irregularity=0.1,
                      border_thickness=1)
         .draw_nuclei(image))
    return image

