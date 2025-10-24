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
    cell_size_from = average_size * 0.004
    cell_size_to = average_size * 0.012

    cell_size = random.randint(cell_size_from, cell_size_to)

    return cell_size

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

def random_elipse_proportion(width, height):


