import numpy as np
import cv2
import math

from src.utils.cancer_nucleus import CancerNucleus


def SingleCellGenerator( size_x=int, size_y=int):


    image = np.zeros((size_x, size_y, 3), dtype=np.uint8)
    cancer_nucleus = CancerNucleus( center=CalculateCenterOfImage(size_x, size_y),
                                    axes=CalculateAxesSizeFromImageSize(size_x, size_y),
                                    angle=np.random.randint(0, 360),
                                    irregularity=0.2,
                                    border_thickness=BorderLineThickness(size_x, size_y))

    cancer_nucleus.draw_nuclei(image)
    cv2.imshow('Nucleus',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def CalculateCenterOfImage(size_x=int, size_y=int):
    center_x = math.floor(size_x / 2)
    center_y = math.floor(size_y / 2)
    return (center_x, center_y)

def CalculateAxesSizeFromImageSize(size_x, size_y):
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

def BorderLineThickness(size_x, size_y):
    base_scale = 3

    mean_size = (size_x + size_y) / 2
    scaling_ratio = mean_size / 100

    adaptive_ratio = math.sqrt(scaling_ratio)+0.5
    scale = max(2, base_scale * adaptive_ratio)
    return int(scale)