from typing import Optional
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

    def with_custom_distribution(self, generator = CenterPointsGenerator) -> 'ImageGenerator':


