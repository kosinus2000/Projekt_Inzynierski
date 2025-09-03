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

def cell_size_proportionally(width, height):
    average_size = (width + height) / 2
    cell_size_from = average_size * 0.004
    cell_size_to = average_size * 0.012

    cell_size = random.randint(cell_size_from, cell_size_to)

    return cell_size

def cell_size():
    cell_size_from = 2
    cell_size_to = 6
    cell_size = random.randint(cell_size_from, cell_size_to)

    return cell_size

