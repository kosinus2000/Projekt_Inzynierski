import random
from abc import ABC, abstractmethod

from src.functions.ellipse_params import ellipse_proportion


class Axes(ABC):
    """
    Represents an abstract base class for managing axes on a 2D coordinate system.

    This class provides the foundation for handling axes placement and scaling.
    It defines an interface for generating axes and a utility for applying the
    ratio to elliptical proportions. Specific implementations must provide the
    logic for axis generation.

    Attributes
    ----------
    x : int
        The x-coordinate of the axis placement.
    y : int
        The y-coordinate of the axis placement.
    size : int
        The size of the axis element.
    """
    def __init__(self, x: int, y: int, size: int, ratio = 0.65):
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
        

class NormalDistributionAxesGenerator(Axes):
    """
    Represents an extension of the Axes class that incorporates generation of
    coordinates following a normal distribution.

    The class allows the creation of axes coordinates derived from a normal
    distribution with a specified standard deviation.

    Attributes
    ----------
    x : int
        The x-coordinate for the initial axis.
    y : int
        The y-coordinate for the initial axis.
    size : int
        The size of the axes.
    dev : int
        The standard deviation for the normal distribution used in generating
        new coordinates.
    """
    def __init__(self,
                 x: int,
                 y: int,
                 size: int,
                 dev : int):
       super().__init__(x, y,size)
       self.dev = dev

    def generate_axes(self):
        gen_x = random.gauss(self.x, self.dev)
        gen_y = random.gauss(self.y, self.dev)
        return int(abs(gen_x)), int(abs(gen_y))

class UniformDistributionAxesGenerator(Axes):
    """
    Summary of what the class does.

    UniformDistributionAxesGenerator is a specialized subclass of the Axes class that generates
    axes values with uniform random distribution within a defined deviation range. This
    class allows users to specify a deviation and subsequently compute randomized axes
    values within the bounds of this deviation. It extends the functionality of the parent
    Axes class by introducing an additional customizable attribute `dev`.

    Attributes
    ----------
    x : int
        The x-coordinate for the base point of the axes.
    y : int
        The y-coordinate for the base point of the axes.
    size : int
        The size of the axes.
    dev : int
        Maximum deviation range for generating randomized axis values.
    """
    def __init__(self,
                 x:int,
                 y:int,
                 dev:int,
                 size:int = 0):
        super().__init__(x, y, size)
        self.dev = dev

    def generate_axes(self):
        ax1 = random.randint(self.x - self.dev, self.x + self.dev)
        ax2 = random.randint(self.y - self.dev, self.y + self.dev)
        return int(abs(ax1)), int(abs(ax2))

