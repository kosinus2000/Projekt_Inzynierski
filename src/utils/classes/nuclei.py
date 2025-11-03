from abc import  ABC
import cv2



class Nuclei(ABC):
    """Represents an abstract base class for drawing nuclei on an image.

    This class provides the necessary attributes and methods to represent
    and render a nucleus with a specified shape, color, and border on an image.

    Attributes:
        center (tuple): Coordinates of the center of the nucleus.
        axes (tuple): Length of the axes of the ellipse representing the nucleus.
        angle (int): Angle of rotation of the ellipse in degrees.
        color (tuple): Color of the nucleus in BGR format.
        thickness (int): Thickness of the nucleus shape. Negative value fills the shape.
        border_color (tuple): Color of the ellipse border in BGR format.
        border_thickness (int): Thickness of the border ellipse. Zero or
            negative value disables the border.
    """

    def __init__(self, center, axes, angle=0, color=(160, 83, 179), thickness=-1, border_color=(107, 26, 121),
                 border_thickness=2):
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
