from src.data_generation.single_cell_generator import CalculateAxesSizeFromImageSize, single_cell_generator_with_open_window
import numpy as np


def training_set_generator(num_pictures : int):
    list_of_pictures = []

    for _ in range(100):
        image = single_cell_generator_with_open_window(64, 64)
        list_of_pictures.append(image)

    training_set = np.array(list_of_pictures)

    training_set = training_set.astype('float32') / 255.0

    return training_set