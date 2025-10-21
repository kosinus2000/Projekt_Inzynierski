"""
A module to represent and draw nuclei shapes on an image using OpenCV.

This module provides a class `Nuclei` that encapsulates details of an
ellipse-like nuclei structure and facilitates drawing it onto an image.
"""

from abc import abstractmethod, ABC
import cv2
import numpy as np

class Nuclei(ABC):

    def __init__(self, center, axes, angle=0, color=(0, 0, 139), thickness=-1, border_color=(0, 0, 80),
                 border_thickness=0):
        self.center = center
        self.axes = axes
        self.angle = angle
        self.color = color
        self.thickness = thickness
        self.border_color = border_color
        self.border_thickness = border_thickness

    def draw_nuclei(self, image):

        cv2.ellipse(image, self.center, self.axes, self.angle, 0, 360, self.color, -1)

        if self.border_thickness > 0:
            cv2.ellipse(image, self.center, self.axes, self.angle, 0, 360, self.border_color, self.border_thickness)
