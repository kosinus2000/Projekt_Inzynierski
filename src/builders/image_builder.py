from typing import Optional
from utils.config import GenerationConfig


class ImageGenerator:

    
    def __init__(self, config: Optional[GenerationConfig] = None):

        self.config = config if config is not None else GenerationConfig()
        self._distribution_strategy = None
        self._axes_strategy = None
        
