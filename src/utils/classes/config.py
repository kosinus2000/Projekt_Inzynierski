from dataclasses import dataclass, field
from typing import Tuple, Optional


@dataclass
class ImageConfig:
    size_x: int = 128
    size_y: int = 128
    backgroundColor: Tuple[int, int, int] = (0, 0, 0)

@dataclass
class NucleusConfig:
    base_color: Tuple[int, int, int] = (160, 83, 179)
    border_color: Tuple[int, int, int] = (107, 26, 121)
    border_thickness: int = 2
    thickness: int = -1
    irregularity: float = 0.3
    color_variation: float = 0.3
    use_perlin_noise: bool = False

@dataclass
class AxesConfig:
    mean_x: int = 10
    mean_y: int = 8
    std_dev: int = 2
    dev: int = 2
    distribution_type: str = 'normal'

@dataclass
class DistributionConfig:
    algorithm: str = 'poisson'
    number_of_points: int = 10
    radius: int = 30
    k: int = 35
    dev: int = 40
    num_clusters: Optional[int] = None
    cell_size: Optional[int] = None

@dataclass
class CellCompositionConfig:
    include_healthy_cells: bool = False
    cancer_config: NucleusConfig = field(default_factory=NucleusConfig)
    healthy_config: Optional[NucleusConfig] = None
    healthy_axes_config: Optional[AxesConfig] = None

@dataclass
class GenerationConfig:
    image: ImageConfig = field(default_factory=ImageConfig)
    nucleus: NucleusConfig = field(default_factory=NucleusConfig)
    axes: AxesConfig = field(default_factory=AxesConfig)
    distribution: DistributionConfig = field(default_factory=DistributionConfig)
    composition: CellCompositionConfig = field(default_factory=CellCompositionConfig)