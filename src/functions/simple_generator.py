import random
import cv2
import numpy as np

from utils.classes.cancer_nucleus import CancerNucleus
from utils.classes.healthy_nucleus import HealthyNucleus


def build(self, show: bool = False) -> np.ndarray:

    width = self.config.image.width
    height = self.config.image.height
    image = np.zeros((height, width, 3), dtype=np.uint8)

    point_gen = self._create_distribution_strategy()
    point_gen.prepare_iterator()
    axes_gen = self._create_axes_strategy()

    use_perlin = self.config.nucleus.use_perlin_noise

    if self.config.composition.include_healthy_cells:
        while True:
            try:
                if random.choice([True, False]):
                    cell = HealthyNucleus(point_gen, axes_gen)
                else:
                    cell = CancerNucleus(
                        point_gen, axes_gen,
                        irregularity=self.config.nucleus.irregularity
                    )

                if use_perlin and isinstance(cell, CancerNucleus):
                    cell.draw_nuclei_with_perlin_noise(image)
                else:
                    cell.draw_nuclei(image)

            except ValueError:
                break
    else:
        while True:
            try:
                cell = CancerNucleus(
                    point_gen, axes_gen,
                    irregularity=self.config.nucleus.irregularity
                )

                if use_perlin:
                    cell.draw_nuclei_with_perlin_noise(image)
                else:
                    cell.draw_nuclei(image)

            except ValueError:
                break

    if show:
        cv2.imshow("Generated Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return image


def build_batch(self, num_images: int, show: bool = False) -> list:

    images = []
    for _ in range(num_images):
        self._distribution_strategy = None
        self._axes_strategy = None
        images.append(self.build(show=show))
    return images
