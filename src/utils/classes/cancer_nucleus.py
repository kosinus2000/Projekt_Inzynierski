import math
import cv2
import numpy as np
import noise

from functions.points_generator import points_generator
from src.utils.classes.nuclei import Nuclei, NucleiTest


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

        safe_center = (int(center[0]), int(center[1]))
        safe_axes = (int(axes[0]), int(axes[1]))

        super().__init__(safe_center, safe_axes, angle, color, thickness)
        self.irregularity = irregularity
        self.border_color = border_color
        self.border_thickness = border_thickness
        self.seed = np.random.randint(0, 100)

    def draw_nuclei(self, image):
        super().draw_nuclei(image)


    def draw_nuclei_with_perlin_noise(self, image):
        """
        Draws nuclei shapes on the provided image using a Perlin noise-based algorithm to
        create irregular and biologically inspired edges.

        This function modifies the input image by overlaying polygonal nuclei shapes that
        simulate natural irregularities using noise values. The function supports color
        customization, border thickness, and rotation of the nuclei shapes.

        Args:
            image (numpy.ndarray): The input image on which the nuclei shapes are drawn.
        """
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


class CancerNucleusTest(NucleiTest):
    _lista_punktów = []
    _licznik = 0
    _liczba_punktów = 0
    def __init__(self, axes_size, irregularity=0.3, angle=0, color=(160, 83, 179),
                 thickness=-1, border_color=(107, 26, 121), border_thickness=2):


        super().__init__(
            center = points_generator(poisson=True)
            , axes_size = axes_size
            , angle = angle
            , color = color
            , thickness = thickness
            , border_color = border_color
            , border_thickness = border_thickness
        )
        self.irregularity = irregularity

    def return_center(self):
        return self.center