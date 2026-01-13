import random
from typing import Optional

import cv2
import numpy as np

from src.utils.classes.axes_distribution_functions import (
    Axes,
    NormalDistributionAxesGenerator,
    UniformDistributionAxesGenerator,
)
from src.utils.classes.center_points import (
    CenterPointsGenerator,
    ClusteredAlgorithmCenterGenerator,
    GaussianAlgorithmCenterGenerator,
    PoissonAlgorithmCenterGenerator,
    RandomAlignmentCenterGenerator,
)
from src.utils.classes.cancer_nucleus import CancerNucleus
from src.utils.classes.healthy_nucleus import HealthyNucleus
from src.utils.classes.config import GenerationConfig, NucleusConfig


class ImageGenerator:
    def __init__(self, config: Optional[GenerationConfig] = None):
        self.config = config if config is not None else GenerationConfig()
        self._distribution_strategy = None
        self._axes_strategy = None

    def with_size(self, width: int, height: int) -> "ImageGenerator":
        self.config.image.width = width
        self.config.image.height = height
        return self

    def with_poisson_distribution(self, radius: int = 30, k: int = 35) -> "ImageGenerator":
        self.config.distribution.algorithm = "poisson"
        self.config.distribution.radius = radius
        self.config.distribution.k = k
        return self

    def with_gaussian_distribution(
        self, num_points: int = 10, deviation: int = 40
    ) -> "ImageGenerator":
        self.config.distribution.algorithm = "gaussian"
        self.config.distribution.number_of_points = num_points
        self.config.distribution.deviation = deviation
        return self

    def with_random_distribution(
        self, num_points: int = 10, cell_size: int = 10
    ) -> "ImageGenerator":
        self.config.distribution.algorithm = "random"
        self.config.distribution.number_of_points = num_points
        self.config.distribution.cell_size = cell_size
        return self

    def with_clustered_distribution(
        self, num_points: int = 10, num_clusters: Optional[int] = None, deviation: int = 40
    ) -> "ImageGenerator":
        self.config.distribution.algorithm = "clustered"
        self.config.distribution.number_of_points = num_points
        self.config.distribution.num_clusters = num_clusters
        self.config.distribution.deviation = deviation
        return self

    def with_cancer_cells(
        self,
        irregularity: float = 0.3,
        color: Optional[tuple] = None,
        border_thickness: int = 2,
    ) -> "ImageGenerator":
        self.config.nucleus.irregularity = irregularity
        if color:
            self.config.nucleus.base_color = color
        self.config.nucleus.border_thickness = border_thickness
        return self

    def with_perlin_noise(self, enabled: bool = True) -> "ImageGenerator":
        self.config.nucleus.use_perlin_noise = enabled
        return self

    def with_axes_config(
        self, mean_x: int = 10, mean_y: int = 8, std_dev: int = 2, distribution: str = "normal"
    ) -> "ImageGenerator":
        self.config.axes.mean_x = mean_x
        self.config.axes.mean_y = mean_y
        self.config.axes.std_dev = std_dev
        self.config.axes.distribution_type = distribution
        return self

    def with_healthy_cells(
        self, enabled: bool = True, color: Optional[tuple] = None
    ) -> "ImageGenerator":
        self.config.composition.include_healthy_cells = enabled
        if color and self.config.composition.healthy_config is None:
            self.config.composition.healthy_config = NucleusConfig(base_color=color)
        return self

    def with_custom_distribution(self, generator: CenterPointsGenerator) -> "ImageGenerator":
        self._distribution_strategy = generator
        return self

    def with_custom_axes(self, axes_generator: Axes) -> "ImageGenerator":
        self._axes_strategy = axes_generator
        return self

    def _create_distribution_strategy(self) -> CenterPointsGenerator:
        if self._distribution_strategy is not None:
            return self._distribution_strategy

        cfg = self.config.distribution
        w, h = self.config.image.width, self.config.image.height

        if cfg.algorithm == "poisson":
            return PoissonAlgorithmCenterGenerator(w, h, cfg.radius, cfg.k)
        elif cfg.algorithm == "gaussian":
            return GaussianAlgorithmCenterGenerator(w, h, cfg.number_of_points, cfg.deviation)
        elif cfg.algorithm == "random":
            return RandomAlignmentCenterGenerator(w, h, cfg.number_of_points, cfg.cell_size or 10)
        elif cfg.algorithm == "clustered":
            return ClusteredAlgorithmCenterGenerator(
                w, h, cfg.number_of_points, cfg.num_clusters, cfg.deviation
            )
        raise ValueError(f"Unknown distribution algorithm: {cfg.algorithm}")

    def _create_axes_strategy(self) -> Axes:
        if self._axes_strategy is not None:
            return self._axes_strategy

        cfg = self.config.axes
        if cfg.distribution_type == "normal":
            return NormalDistributionAxesGenerator(cfg.mean_x, cfg.mean_y, 0, cfg.std_dev)
        elif cfg.distribution_type == "uniform":
            return UniformDistributionAxesGenerator(cfg.mean_x, cfg.mean_y, cfg.deviation)
        raise ValueError(f"Unknown axes distribution: {cfg.distribution_type}")

    def build(self, show: bool = False) -> np.ndarray:
        w, h = self.config.image.width, self.config.image.height
        image = np.zeros((h, w, 3), dtype=np.uint8)

        point_gen = self._create_distribution_strategy()
        point_gen.prepare_iterator()
        axes_gen = self._create_axes_strategy()
        use_perlin = self.config.nucleus.use_perlin_noise

        while True:
            try:
                if self.config.composition.include_healthy_cells and random.random() < 0.5:
                    cell = HealthyNucleus(point_gen, axes_gen)
                else:
                    cell = CancerNucleus(
                        point_gen, axes_gen, irregularity=self.config.nucleus.irregularity
                    )

                # Perlin noise disabled due to OpenCV memory issues on Windows
                # if use_perlin and isinstance(cell, CancerNucleus):
                #     cell.draw_nuclei_with_perlin_noise(image)
                # else:
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