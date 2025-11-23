import math


def border_line_thickness(size_x, size_y):
    base_scale = 3

    mean_size = (size_x + size_y) / 2
    scaling_ratio = mean_size / 100

    adaptive_ratio = math.sqrt(scaling_ratio)+0.3
    scale = max(2, base_scale * adaptive_ratio)
    return int(scale)
