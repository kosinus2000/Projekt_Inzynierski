import numpy as np

from src.builders.image_builder import ImageGenerator
from builders.config import GenerationConfig


def generate_image(
    width: int = 128,
    height: int = 128,
    algorithm: str = "poisson",
    irregularity: float = 0.3,
    use_perlin_noise: bool = False,
    random_colors: bool = False,
    show: bool = False,
    ) -> np.ndarray:

    generator = ImageGenerator()

    generator.with_size(width, height)
    generator.with_cancer_cells(irregularity=irregularity, random_colors=random_colors)

    if algorithm == "poisson":
        generator.with_poisson_distribution()
    elif algorithm == "gaussian":
        generator.with_gaussian_distribution()
    elif algorithm == "random":
        generator.with_random_distribution()
    elif algorithm == "clustered":
        generator.with_clustered_distribution()

    if use_perlin_noise:
        generator.with_perlin_noise()

    return generator.build(show=show)


def generate_batch(
    num_images: int,
    width: int = 128,
    height: int = 128,
    algorithm: str = "poisson",
    irregularity: float = 0.3,
    use_perlin_noise: bool = False,
    random_colors: bool = False,
    ) -> list:
    generator = ImageGenerator()

    generator.with_size(width, height)
    generator.with_cancer_cells(irregularity=irregularity, random_colors=random_colors)

    if algorithm == "poisson":
        generator.with_poisson_distribution()
    elif algorithm == "gaussian":
        generator.with_gaussian_distribution()
    elif algorithm == "random":
        generator.with_random_distribution()
    elif algorithm == "clustered":
        generator.with_clustered_distribution()

    if use_perlin_noise:
        generator.with_perlin_noise()

    return generator.build_batch(num_images)


def generate_with_config(config: GenerationConfig, show: bool = False) -> np.ndarray:
    return ImageGenerator(config).build(show=show)