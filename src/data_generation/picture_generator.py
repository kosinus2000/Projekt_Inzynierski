import random
import cv2
import numpy as np

from src.functions.ellipse_params import ellipse_proportion, cell_size, cell_size_proportionally
from src.utils.classes.cancer_nucleus import CancerNucleus
from src.functions.poisson_sampling import poisson_sampling


def generate_picture_with_Poisson_sampling(width: int = 500, height: int = 500, proportionally: bool = False):
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
    image = np.zeros((height, width, 3), np.uint8)



    for center_point in points:
        if proportionally:
            nuclei_size = cell_size_proportionally(width, height)

        else:
            nuclei_size = cell_size()
        axes = ellipse_proportion(nuclei_size)
        angle = random.randint(0, 360)

        center = (int(center_point[0]), int(center_point[1]))
        axes = (int(axes[0]), int(axes[1]))

        (CancerNucleus(center=center_point,
                      axes= axes,
                      angle = angle,
                      thickness = -1,
                      irregularity=0.1,
                      border_thickness=1)
         .draw_nuclei(image))
    return image

def generate_picture_with_rows_and_columns (rows: int, columns: int, method_to_generate):
    """
    Generates a grid of pictures and displays it in a window.

    This function creates a specified number of pictures using a provided method,
    organizes those pictures into a grid based on the specified number of rows and
    columns, and displays the resulting grid using OpenCV. The method to generate
    the pictures must produce individual picture objects suitable for inclusion in
    the grid.

    Args:
        rows: Number of rows in the grid representing pictures.
        columns: Number of columns in the grid representing pictures.
        method_to_generate: Callable used to generate individual pictures.

    Raises:
        ValueError: If rows or columns are not positive integers.
        TypeError: If method_to_generate is not callable.
    """
    pictures = [method_to_generate() for i in range(rows * columns)]

    pictures_grid = [pictures[i : i + columns] for i in range(0, len(pictures), columns)]

    lista_polaczonych_rzedow = [np.hstack(rzad) for rzad in pictures_grid]
    grid = np.vstack(lista_polaczonych_rzedow)
    cv2.imshow('picture', grid)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def generate_image_with_random_aligment(width: int = 128, height: int = 128):

    image = np.zeros((width, height, 3), dtype=np.uint8)

    pixel_density = 2500
    total_area = width * height
    num_cells = int(total_area / pixel_density)

    lista = []

    for _ in range(num_cells):
        x = random.uniform(0, width)
        y = random.uniform(0, height)
        p = [int(x), int(y)]
        lista.append(p)


    cell_size  = cell_size_proportionally(width, height)
    axes = ellipse_proportion(cell_size)
    angle = random.randint(0, 360)

    for point in lista:
        center = (int(point[0]), int(point[1]))
        cell_size = cell_size_proportionally(width, height)
        axes = ellipse_proportion(cell_size)
        angle = random.randint(0, 360)

        (CancerNucleus(center=center,
                      axes=axes,
                      angle=angle,
                      thickness=-1,
                      irregularity=0.1,
                      border_thickness=1)
         .draw_nuclei(image))

    return image


def show_image(image):
    cv2.imshow('picture', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()