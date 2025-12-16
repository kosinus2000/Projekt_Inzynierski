from src.utils.classes.nuclei import Nuclei

class HealthyNucleus(Nuclei):
    """
    Represents a healthy nucleus with specific visual properties and rendering
    methods.

    The HealthyNucleus class is a specialized subclass of the Nuclei class. It
    inherits attributes and methods to define the appearance of a healthy nucleus
    and manage its rendering in a graphical context. This implementation allows
    you to specify the nucleus's geometric parameters, colors, and border styles.

    Attributes:
        center (tuple[int, int]): Coordinates of the center of the nucleus.
        axes (tuple[int, int]): Lengths of the axes of the nucleus (major and minor).
        angle (int): Angle of rotation of the nucleus.
        color (tuple[int, int, int]): Color of the nucleus.
        thickness (int): Thickness of the outline of the nucleus.
        border_color (tuple[int, int, int]): Color of the nucleus's border.
        border_thickness (int): Thickness of the border of the nucleus.
    """

    def __init__(self, center, axes, angle=0, color=(160, 83, 179), thickness=-1, border_color=(107, 26, 121),
                 border_thickness=2):
        super().__init__(center, axes, angle, color, thickness, border_color, border_thickness)

    def draw_nuclei(self, image):
        super().draw_nuclei(image)