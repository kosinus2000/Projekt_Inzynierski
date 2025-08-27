from src.utils.nuclei import Nuclei


class HealthyNucleus(Nuclei):
    def __init__(self, center, axes, angle=0, color=(255,255,255), thickness=-1):
        super().__init__(center, axes, angle, color, thickness)

    def draw_nuclei(self, image):
        super().draw_nuclei(image)