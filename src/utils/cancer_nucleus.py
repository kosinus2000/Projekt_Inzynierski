import math
import cv2
import numpy as np
import noise

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

    def __init__(self, center, axes, angle=0, color=(160, 83, 179), thickness=-1, irregularity=0.3,
                 border_color=(107, 26, 121), border_thickness=2):
        super().__init__(center, axes, angle, color, thickness)
        self.irregularity = irregularity
        self.border_color = border_color
        self.border_thickness = border_thickness
        self.seed = np.random.randint(0, 100)

    def draw_nuclei(self, image):
        cx, cy = self.center
        ax, ay = self.axes
        angle = np.deg2rad(self.angle)

        points = []
        num_points = 1000

        for i in range(num_points):
            t = 2 * math.pi * i / num_points
            x = ax * np.cos(t)
            y = ay * np.sin(t)

            perlin_value = noise.pnoise1(t * 2.0,
                                         octaves=4,
                                         persistence=0.5,
                                         lacunarity=3.0,
                                         repeat=1024,
                                         base=self.seed)
            factor = 1 + self.irregularity * perlin_value

            x *= factor
            y *= factor

            xr = x * np.cos(angle) - y * np.sin(angle)
            yr = x * np.sin(angle) + y * np.cos(angle)

            points.append([int(cx + xr), int(cy + yr)])

        points = np.array(points, dtype=np.int32).reshape((-1, 1, 2))
        cv2.fillPoly(image, [points], self.color)
        if self.border_thickness > 0:
            cv2.polylines(image, [points], isClosed=True, color=self.border_color, thickness=self.border_thickness)
