import random
from abc import ABC, abstractmethod

import numpy as np


class NumbersOfPoints(ABC):
    """Abstract base class for generating variable number of points with deviation."""

    def __init__(self, number_of_points: int, deviation: int) -> None:
        """Initialize point generator.
        
        Args:
            number_of_points: Base number of points to generate
            deviation: Acceptable deviation from base number
            
        Raises:
            ValueError: If number_of_points <= 0 or deviation < 0
        """
        if number_of_points <= 0:
            raise ValueError("number_of_points must be greater than 0")
        if deviation < 0:
            raise ValueError("deviation must be non-negative")
            
        self.number_of_points = number_of_points
        self.deviation = deviation

    @abstractmethod
    def calculate_number_of_points(self) -> int:
        """Calculate and return the number of points with applied deviation."""
        pass

class UniformPointGenerator(NumbersOfPoints):
    """Generates random number of points using uniform distribution."""
    
    def calculate_number_of_points(self) -> int:
        """Returns a random integer within deviation range.
        
        Ensures result is always at least 1 to avoid invalid point counts.
        """
        start = max(1, self.number_of_points - self.deviation)
        end = self.number_of_points + self.deviation
        return random.randint(start, end)

class NormalPointGenerator(NumbersOfPoints):
    """Generates random number of points using normal distribution."""
    
    def calculate_number_of_points(self) -> int:
        """Returns integer sampled from normal distribution.
        
        Ensures result is always at least 1 to avoid invalid point counts.
        """
        sample = np.random.normal(loc=self.number_of_points, scale=self.deviation)
        return max(1, int(round(sample)))