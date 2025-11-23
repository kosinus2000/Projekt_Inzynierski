from abc import ABC
import cv2


class Nuclei(ABC):
    """Represents an abstract base class for drawing nuclei on an image."""

    def __init__(self, center, axes, angle=0, color=(160, 83, 179), thickness=-1, border_color=(107, 26, 121),
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