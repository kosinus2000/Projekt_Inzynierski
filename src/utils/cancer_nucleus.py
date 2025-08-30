import math
import random as pyrandom
import cv2
import numpy as np

from src.utils.nuclei import Nuclei


class CancerNucleus(Nuclei):
    """Represents a cancerous nucleus with custom irregularity and styling attributes.

    This class extends the Nuclei class, adding the functionality to render an
    irregular ellipsoidal shape. The irregular nature of the shape is controlled by
    the irregularity attribute, which introduces variations in the geometry of the
    ellipsoid. It also allows customization of color, thickness, border color, and
    border thickness of the rendered nucleus.

    Attributes:
        irregularity (float): The factor controlling the irregularity of the nuclear
            shape. Higher values yield more irregular outlines.
    """
    def __init__(self, center, axes, angle=0, color=(20, 0, 100), thickness=-1, irregularity=0.3,
                 border_color=(0, 0, 0), border_thickness=2):
        super().__init__(center, axes, angle, color, thickness, border_color, border_thickness)
        self.irregularity = irregularity

    def draw_nuclei(self, image):
        cx, cy = self.center
        a, b = self.axes

        a, b = int(a), int(b)
        angle = float(self.angle)
        angle_rad = np.deg2rad(angle)

        points = []
        num_points = 1000

        for i in range(num_points):
            t = 2 * math.pi * i / num_points

            scale_a = a * (1 + self.irregularity * (pyrandom.uniform(-0.2, 0.2)))
            scale_b = b * (1 + self.irregularity * (pyrandom.uniform(-0.2, 0.2)))

            x = scale_a * np.cos(t)
            y = scale_b * np.sin(t)

            if self.irregularity > 0:
                extra_noise = 1 + (self.irregularity * 0.1) * (
                        0.5 * np.sin(8 * t) +
                        0.5 * (pyrandom.random() - 0.5)
                )
                x *= extra_noise
                y *= extra_noise

            xr = x * np.cos(angle_rad) - y * np.sin(angle_rad)
            yr = x * np.sin(angle_rad) + y * np.cos(angle_rad)

            points.append([int(cx + xr), int(cy + yr)])

        points = np.array(points, dtype=np.int32).reshape((-1, 1, 2))

        cv2.fillPoly(image, [points], self.color)

        if self.border_thickness > 0:
            cv2.polylines(image, [points], isClosed=True, color=self.border_color, thickness=self.border_thickness)