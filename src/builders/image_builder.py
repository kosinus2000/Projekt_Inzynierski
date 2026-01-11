from typing import Optional
from utils.classes.config import GenerationConfig


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

