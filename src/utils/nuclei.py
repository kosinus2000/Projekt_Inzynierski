import cv2
import numpy as np

class Nuclei:

    def __init__(self, center, axes, angle= 0, color = (255,255,255), thickness = -1):
        self.center = center
        self.axes = axes
        self.angle = angle
        self.color = color
        self.thickness = thickness

    def draw_nuclei(self, image):
        cv2.ellipse(image, self.center, self.axes, self.angle, 0, 360, self.color, self.thickness)