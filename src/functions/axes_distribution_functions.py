import random
from abc import ABC, abstractmethod

from functions.ellipse_params import ellipse_proportion


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
    def generate_axes(self) -> [int, int]:
        pass

    def use_ratio(self):
        return ellipse_proportion(self.size, self.ratio)
        

class AxesWithNormalDistribution(Axes):
    def __init__(self, x, y, dev):
       super().__init__(x, y)
       self.dev = dev

    def generate_axes(self):
        gen_x = random.gauss(self.x, self.dev)
        gen_y = random.gauss(self.y, self.dev)
        return int(gen_x), int(gen_y)

class AxesWithUniformDistribution(Axes):
    def __init__(self, x, y, dev):
        super().__init__(x, y)
        self.dev = dev

    def generate_axes(self):
        return random.randint(self.x - self.dev,  self.x + self.dev), random.randint(self.y - self.dev, self.y + self.dev)
