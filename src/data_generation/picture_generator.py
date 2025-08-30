import random
import cv2
import numpy as np

from src.functions.ellipse import ellipse_proportion
from src.utils.cancer_nucleus import CancerNucleus
from src.utils.poisson_sampling import poisson_sampling


def generate_picture(width = 500, height = 500):
    """
    Generates an image with randomly sampled ellipses that simulate cell nuclei.

    This function employs Poisson disk sampling to generate random points, which
    serve as the centers for ellipses representing cell nuclei. It then draws these
    ellipses on a blank image of the specified size.

    Args:
        width (int, optional): The width of the generated image in pixels. Defaults to 500.
        height (int, optional): The height of the generated image in pixels. Defaults to 500.

    Returns:
        np.ndarray: A 3D array representing the generated image with drawn nuclei.
    """
    points = poisson_sampling(width, height, 10)
    image = np.zeros((width, height, 3), np.uint8)
    for center_point in points:
        axes = ellipse_proportion(random.randint(2,4))
        angle = random.randint(0, 360)

        (CancerNucleus(center=center_point,
                      axes= axes,
                      angle = angle, color =(20, 0, 100),
                      thickness = -1,
                      irregularity=0.3,
                      border_color=(0, 0, 0),
                      border_thickness=2)
         .draw_nuclei(image))
    return image

