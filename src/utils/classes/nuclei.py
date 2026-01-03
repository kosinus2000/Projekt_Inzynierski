import random
from abc import ABC

import cv2
import numpy as np

from src.functions.axes_distribution_functions import Axes
from src.functions.center_points import CenterPointsGenerator
from src.functions.poisson_sampling import poisson_sampling


class Nuclei(ABC):
    """Represents an abstract base class for drawing nuclei on an image."""

    def __init__(self, center : str, axes, angle=0, color=(160, 83, 179), thickness=-1, border_color=(107, 26, 121),
                 border_thickness=2):
        self.center = (int(center[0]), int(center[1]))
        self.axes = (int(axes[0]), int(axes[1]))

        self.angle = angle
        self.color = color
        self.thickness = thickness
        self.border_color = border_color
        self.border_thickness = border_thickness

    def draw_nuclei(self, image):
        cv2.ellipse(image, self.center, self.axes, self.angle, 0, 360, self.color, self.thickness)

        if self.border_thickness > 0:
            cv2.ellipse(image, self.center, self.axes, self.angle, 0, 360, self.border_color, self.border_thickness)


class NucleiTest(ABC):

    def __init__(self,
                 point_generator_instance: CenterPointsGenerator,
                 axes_generator_instance: Axes,
                 angle= None,
                 color=(160, 83, 179),
                 thickness=-1,
                 border_color=(107, 26, 121),
                 border_thickness=2):
        self.center = point_generator_instance.get_next_point()

        if self.center is None:
            raise ValueError("No more points to generate")

        self.axes = axes_generator_instance.generate_axes()
        self.angle = angle if angle is not None else random.randint(0, 360)
        self.color = color
        self.thickness = thickness
        self.border_color = border_color
        self.border_thickness = border_thickness

    def draw_nuclei(self, image):
        cv2.ellipse(image, self.center, self.axes, self.angle, 0, 360, self.color, self.thickness)

        if self.border_thickness > 0:
            cv2.ellipse(image, self.center, self.axes, self.angle, 0, 360, self.border_color, self.border_thickness)
