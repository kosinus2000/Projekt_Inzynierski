import random

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

