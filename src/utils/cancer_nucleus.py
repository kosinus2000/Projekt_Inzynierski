import math
import random as pyrandom
import cv2
import numpy as np

from src.utils.nuclei import Nuclei

class CancerNucleus(Nuclei):
    def __init__(self, center, axes, angle=0, color=(200, 200, 255), thickness=-1, irregularity=0.3):

        super().__init__(center, axes, angle, color, thickness)
        self.irregularity = irregularity

    def draw_nuclei(self, image):
        cx, cy = self.center
        a, b = self.axes
        angle =np.deg2rad( self.angle)


        points = []
        num_points = 1000

        for i in range(num_points):
            t = 2 * math.pi * i / num_points
            x = a * np.cos(t)
            y = b * np.sin(t)

            factor = 1 + self.irregularity * (0.3*np.sin(6*t) + 0.7*(pyrandom.random()-0.5))
            x *= factor
            y *= factor

            xr = x * np.cos(angle) - y * np.sin(angle)
            yr = x * np.sin(angle) + y * np.cos(angle)

            points.append([int(cx + xr), int(cy + yr)])

        points = np.array(points, dtype=np.int32).reshape((-1, 1, 2))

        if self.thickness < 0:
            # wypełnij kształt (jak -1 w ellipse)
            cv2.fillPoly(image, [points], self.color)
        else:
            # sam kontur o zadanej grubości
            cv2.polylines(image, [points], isClosed=True, color=self.color, thickness=self.thickness)