import random
from abc import ABC, abstractmethod

from src.functions.ellipse_params import ellipse_proportion


class Axes(ABC):
    def __init__(self, x, y, size, ratio = 0.65):
        self.x = x
        self.y = y
        self.size = size
        self._ratio = ratio

    @property
    def ratio(self):
        return self._ratio
    @ratio.setter
    def ratio(self, value):
        self._ratio = value

    @abstractmethod
    def generate_axes(self) -> tuple[int, int]:
        pass

    def use_ratio(self):
        return ellipse_proportion(self.size, self.ratio)
        

class AxesWithNormalDistribution(Axes):
    def __init__(self, x, y,size, dev):
       super().__init__(x, y,size)
       self.dev = dev

    def generate_axes(self):
        gen_x = random.gauss(self.x, self.dev)
        gen_y = random.gauss(self.y, self.dev)
        return int(abs(gen_x)), int(abs(gen_y))

class AxesWithUniformDistribution(Axes):
    def __init__(self, x, y,size, dev):
        super().__init__(x, y, size)
        self.dev = dev

    def generate_axes(self):
        ax1 = random.randint(self.x - self.dev, self.x + self.dev)
        ax2 = random.randint(self.y - self.dev, self.y + self.dev)
        return int(abs(ax1)), int(abs(ax2))

