from src.utils.nuclei import Nuclei

class HealthyNucleus(Nuclei):
    def __init__(self, center, axes, angle=0, color=(160, 83, 179), thickness=-1, border_color=(107, 26, 121),
                 border_thickness=2):
        super().__init__(center, axes, angle, color, thickness, border_color, border_thickness)

    def draw_nuclei(self, image):
        super().draw_nuclei(image)