"""
A module for performing a variety of geometric calculations related to ellipses
and cell proportions. Provides functions for scaling dimensions and generating
randomized values for cell and axis sizes.

"""
import math
import random

import numpy as np


def ellipse_proportion(x):
    """
    Calculates and returns the dimensions of an ellipse proportionally scaled from
    the given input.

    Args:
        x (float): The width of the ellipse.

    Returns:
        tuple: A tuple containing the integer width and height of the scaled ellipse.
    """
    ratio = 0.65
    y = x * 0.65
    return (int(x), int(y))

def cell_size_proportionally(width : int, height : int):
    """
    Calculates the cell size proportionally based on the provided width and height.

    This function computes an average size from the given width and height, determines
    a proportional range for the cell size, and selects a random value within this
    range as the cell size.

    Args:
        width: The width of the object.
        height: The height of the object.

    Returns:
        int: A randomly chosen cell size within the calculated proportional range.
    """
    average_size = (width + height) / 2

    raw_from = int(average_size * 0.07)
    raw_to = int(average_size * 0.17)

    cell_size_from = max(1, raw_from)
    cell_size_to = max(cell_size_from, raw_to)

    return random.randint(cell_size_from, cell_size_to)

def cell_size():
    """
    Generates a random cell size within a specified range.

    This function selects a random integer value representing the size of a
    cell. The size is determined by a predefined range specified within the
    function.

    Returns:
        int: A randomly selected integer representing the cell size.
    """
    cell_size_from = 2
    cell_size_to = 6
    cell_size = random.randint(cell_size_from, cell_size_to)

    return cell_size


def calculate_center_of_image(size_x=int, size_y=int):
    """
    Calculates the center coordinates of an image based on its dimensions.

    This function takes the width and height of an image and calculates the
    coordinates of its center point. It uses the floor division to ensure that
    the result is an integer.

    Args:
        size_x (int): The width of the image.
        size_y (int): The height of the image.

    Returns:
        tuple: A tuple containing the x and y coordinates of the center point
        of the image as integers.
    """
    center_x = math.floor(size_x / 2)
    center_y = math.floor(size_y / 2)
    return (center_x, center_y)

def calculate_axes_size_from_image_size(size_x, size_y):
    """
    Calculates the optimal sizes of axes based on input image dimensions. This function takes the
    dimensions of an image and computes axes sizes by scaling them adaptively, factoring in
    random variation to simulate realistic sizing conditions. The computation maintains minimum
    values for the axes to ensure valid results.

    Args:
        size_x (float): Width of the input image.
        size_y (float): Height of the input image.

    Returns:
        tuple: A tuple containing the calculated sizes of the two axes as integers.
    """

    a = size_x *0.3
    b = size_y *0.195

    base_scale = 3
    standard_avg_size = 200
    mean_size = (size_x + size_y) / 2
    scaling_ratio = mean_size / standard_avg_size

    adaptive_ratio = math.sqrt(scaling_ratio)
    scale = max(2, base_scale * adaptive_ratio)

    axis_a = np.random.normal(loc=a, scale= 2 )
    axis_b = np.random.normal(loc=b, scale= scale )

    return (int(max(1, axis_a)), int(max(1, axis_b)))


