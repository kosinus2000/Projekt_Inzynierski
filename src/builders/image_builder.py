from typing import Optional

from utils.classes.axes_distribution_functions import Axes, UniformDistributionAxesGenerator, \
    NormalDistributionAxesGenerator
from utils.classes.center_points import CenterPointsGenerator, GaussianAlgorithmCenterGenerator, \
    PoissonAlgorithmCenterGenerator, RandomAlignmentCenterGenerator, ClusteredAlgorithmCenterGenerator
from utils.classes.config import GenerationConfig, NucleusConfig


class ImageGenerator:

    
    def __init__(self, config: Optional[GenerationConfig] = None):

        self.config = config if config is not None else GenerationConfig()
        self._distribution_strategy = None
        self._axes_strategy = None
        
    def with_size(self, size_x: int, size_y: int) -> 'ImageGenerator':
        self.config.image.size_y = size_y
        self.config.image.size_x = size_x
        return self

    def with_gaussian_distribution(self, num_points: int = 10, dev: int = 40 )-> 'ImageGenerator':
        self.config.distribution.num_points = num_points
        self.config.distribution.dev = dev
        self.config.distribution.algorithm = 'gaussian'
        return self

    def with_poisson_distribution(self, k: int = 35, radius: int = 30)-> 'ImageGenerator':
        self.config.distribution.k = k
        self.config.distribution.radius = radius
        self.config.distribution.algorithm = 'poisson'
        return self

    def with_random_distribution(self, num_points: int = 10, cell_size: int = 10) -> 'ImageGenerator':
        self.config.distribution.num_points = num_points
        self.config.distribution.cell_size = cell_size
        self.config.distribution.algorithm = 'random'
        return self

    def with_clustered_distribution(self, num_points: int = 10, num_clusters: Optional[int] = None,
                                    dev: int = 40) -> 'ImageGenerator':
        self.config.distribution.num_points = num_points
        self.config.distribution.num_clusters = num_clusters
        self.config.distribution.dev = dev
        self.config.distribution.algorithm = 'clustered'
        return self

    def with_perlin_noice(self, endabled: bool = True) -> 'ImageGenerator':
        self.config.nucleus.use_perlin_noise = endabled
        return self

    def with_axes_config(self, mean_x:int = 10, mean_y : int = 8, std_dev: int = 2, distribution : str ='normal' ) -> 'ImageGenerator':
        self.config.axes.mean_x = mean_x
        self.config.axes.mean_y = mean_y
        self.config.axes.std_dev = std_dev
        self.config.distribution.distribution = distribution
        return self

    def with_healthy_cells(self, enabled: bool = True, color: Optional[tuple]= None) -> 'ImageGenerator':
        self.config.composition.include_healthy_cells = enabled
        if color and self.config.composition.healthy_config is None:
            self.config.composition.healthy_config = NucleusConfig(base_color=color)

        return self

    def with_custom_distribution(self, generator: CenterPointsGenerator) -> 'ImageGenerator':
        self._distribution_strategy = generator
        return self

    def with_custom_axes(self, axes_gen: Axes) -> 'ImageGenerator':
        if self._axes_strategy is None:
            self._axes_strategy = axes_gen
        return self

    def with_cancers_cells(self, irregularity : float = 0.3,
                           color: Optional[tuple]= None,
                           border_thickness : int = 2) -> 'ImageGenerator':
        self.config.nucleus.irregularity = irregularity
        self.config.nucleus.color = color
        self.config.nucleus.border_thickness = border_thickness
        return self

    def _create_distribution_strategy(self) -> CenterPointsGenerator:
        if self._distribution_strategy is None:
            return self._distribution_strategy

        cen_points_gen =self.config.distribution
        width = self.config.image.size_x
        height = self.config.image.size_y

        if cen_points_gen.algorithm == 'gaussian':
            return GaussianAlgorithmCenterGenerator(width, height, cen_points_gen.number_of_points, cen_points_gen.dev)
        elif cen_points_gen.algorithm == 'poisson':
            return PoissonAlgorithmCenterGenerator(width, height, cen_points_gen.number_of_points, cen_points_gen.dev)
        elif cen_points_gen.algorithm == 'random':
            cell_size = cen_points_gen.cell_size or 10
            return RandomAlignmentCenterGenerator(width, height,cen_points_gen.number_of_points, cell_size)
        elif cen_points_gen.algorithm == 'clustered':
            return ClusteredAlgorithmCenterGenerator(width, height, cen_points_gen.number_of_points,cen_points_gen.num_clusters, cen_points_gen.dev)
        else:
            raise ValueError(f'Unknown distribution strategy {cen_points_gen.algorithm}')

    def _create_axes_strategy(self) -> Axes:
        """Create axes generation strategy based on configuration."""
        if self._axes_strategy is not None:
            return self._axes_strategy

        cen_points_gen = self.config.axes

        if cen_points_gen.distribution_type == 'normal':
            return NormalDistributionAxesGenerator(cen_points_gen.mean_x, cen_points_gen.mean_y, 0, cen_points_gen.std_dev)
        elif cen_points_gen.distribution_type == 'uniform':
            return UniformDistributionAxesGenerator(cen_points_gen.mean_x, cen_points_gen.mean_y, cen_points_gen.deviation)
        else:
            raise ValueError(f"Unknown axes distribution: {cen_points_gen.distribution_type}")

    def br