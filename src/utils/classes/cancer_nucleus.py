import math

import cv2
import numpy as np

from src.utils.classes.nucleus import NucleiOld, Nuclei
from src.utils.cell_settings import generate_color_variation_normal


class CancerNucleusOld(NucleiOld):
    """Represents a cancerous nucleus with custom irregularity and styling attributes.

    This class extends the NucleiOld class, adding the functionality to render an
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
        Draws nuclei shapes with smooth, biological irregularities.
        """
        if self.center is None or self.axes is None:
            return
        cx, cy = self.center
        ax, ay = self.axes
        angle = np.deg2rad(self.angle)

        rng = np.random.RandomState(self.seed)
        
        points = []
        num_points = 128

        num_waves = 5
        noise_values = np.array([rng.uniform(-1, 1) for _ in range(num_waves)])
        
        for i in range(num_points):
            t = 2 * math.pi * i / num_points
            x = ax * np.cos(t)
            y = ay * np.sin(t)

            phase = (t / (2 * math.pi)) * num_waves
            idx = int(phase) % num_waves
            next_idx = (idx + 1) % num_waves
            alpha = phase - int(phase)
            
            cos_alpha = (1 - np.cos(alpha * math.pi)) / 2
            perlin_like = (1 - cos_alpha) * noise_values[idx] + cos_alpha * noise_values[next_idx]
            
            factor = 1 + perlin_like * self.irregularity * 0.4

            x *= factor
            y *= factor

            xr = x * np.cos(angle) - y * np.sin(angle)
            yr = x * np.sin(angle) + y * np.cos(angle)

            px = int(cx + xr)
            py = int(cy + yr)
            px = int(np.clip(px, 0, image.shape[1] - 1))
            py = int(np.clip(py, 0, image.shape[0] - 1))
            points.append([px, py])

        points = np.array(points, dtype=np.int32)
        cv2.drawContours(image, [points], 0, self.color, -1)
        if self.border_thickness > 0:
            cv2.drawContours(image, [points], 0, self.border_color, self.border_thickness)


class CancerNucleus(Nuclei):
    def __init__(self,
                 point_generator_instance,
                 axes_generator_instance,
                 irregularity=0.3,
                 color = None,
                 border_color = None,
                 **kwargs):

        self.irregularity = irregularity
        self.seed = np.random.randint(0, 100000)

        if color is None:
            color = generate_color_variation_normal((160, 83, 179))

        if border_color is None:
            border_color = generate_color_variation_normal((107, 26, 121))

        super().__init__(
            point_generator_instance=point_generator_instance,
            axes_generator_instance=axes_generator_instance,
            color = color,
            border_color = border_color,
            **kwargs
        )




    def draw_nuclei_with_perlin_noise(self, image):
        """
        Draws nuclei shapes with subtle, biological irregularities.
        Maintains elliptical base with gentle deformations like real biopsy samples.
        """
        if self.center is None or self.axes is None:
            return
        
        cx, cy = self.center
        ax, ay = self.axes
        angle = np.deg2rad(self.angle)

        rng = np.random.RandomState(self.seed)
        
        points = []
        num_points = 128

        num_waves = 5
        noise_values = np.array([rng.uniform(-1, 1) for _ in range(num_waves)])
        
        for i in range(num_points):
            t = 2 * math.pi * i / num_points
            x = ax * np.cos(t)
            y = ay * np.sin(t)

            phase = (t / (2 * math.pi)) * num_waves
            idx = int(phase) % num_waves
            next_idx = (idx + 1) % num_waves
            alpha = phase - int(phase)
            
            cos_alpha = (1 - np.cos(alpha * math.pi)) / 2
            perlin_like = (1 - cos_alpha) * noise_values[idx] + cos_alpha * noise_values[next_idx]
            
            factor = 1 + perlin_like * self.irregularity * 0.4

            x *= factor
            y *= factor

            xr = x * np.cos(angle) - y * np.sin(angle)
            yr = x * np.sin(angle) + y * np.cos(angle)

            px = int(cx + xr)
            py = int(cy + yr)
            px = int(np.clip(px, 0, image.shape[1] - 1))
            py = int(np.clip(py, 0, image.shape[0] - 1))
            points.append([px, py])

        points = np.array(points, dtype=np.int32)
        cv2.drawContours(image, [points], 0, self.color, -1)
        if self.border_thickness > 0:
            cv2.drawContours(image, [points], 0, self.border_color, self.border_thickness)