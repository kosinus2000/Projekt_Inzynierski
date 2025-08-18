import cv2

from src.utils.nuclei import Nuclei


class CancerNucleus(Nuclei):
    def __init__(self, center, axes, angle=0, color=(200, 200, 255), thickness=-1, irregularity=0.3):

        super().__init__(center, axes, angle, color, thickness)
        self.irregularity = irregularity

    def draw_nuclei(self, image):
        super().draw_nuclei(image)