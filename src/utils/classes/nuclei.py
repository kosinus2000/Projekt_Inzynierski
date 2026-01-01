import random
from abc import ABC
import cv2

from functions.poisson_sampling import poisson_sampling


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
    _list_of_points = []
    _counter = 0
    _number_of_points = 0

    def __init__(self,
                 center,
                 axes_size,
                 angle= random.randint(0, 360),
                 color=(160, 83, 179),
                 thickness=-1,
                 border_color=(107, 26, 121),
                 border_thickness=2):

        self.center = center
        self.axes_size = axes_size
        self.angle = angle
        self.color = color
        self.thickness = thickness
        self.border_color = border_color
        self.border_thickness = border_thickness

    # @staticmethod
    # def points_generator(poisson=False):
    #     if poisson:
    #         if not NucleiTest._list_of_points:
    #             NucleiTest._list_of_points = poisson_sampling(128, 128)
    #
    #         if NucleiTest._counter < len(NucleiTest._list_of_points):
    #             center = NucleiTest._list_of_points[NucleiTest._counter]
    #             NucleiTest._counter += 1
    #             return center
    #         else:
    #             NucleiTest._counter = 0
    #             return NucleiTest.points_generator(poisson=True)
    #     return (0, 0)

    def return_center(self):
        return self.center

    def draw_nuclei(self, image):
        cv2.ellipse(image, self.center, self.axes, self.angle, 0, 360, self.color, self.thickness)

        if self.border_thickness > 0:
            cv2.ellipse(image, self.center, self.axes, self.angle, 0, 360, self.border_color, self.border_thickness)
