import math
import numpy as np


def border_line_thickness(size_x, size_y):
    base_scale = 3

    mean_size = (size_x + size_y) / 2
    scaling_ratio = mean_size / 100

    adaptive_ratio = math.sqrt(scaling_ratio)+0.3
    scale = max(2, base_scale * adaptive_ratio)
    return int(scale)


def generate_color_variation_normal(base_color, std_dev=20):

    varied_color = []
    for channel in base_color:
        variation = np.random.normal(0, std_dev)
        new_value = np.clip(channel + variation, 0, 255)
        varied_color.append(int(new_value))

    return tuple(varied_color)
