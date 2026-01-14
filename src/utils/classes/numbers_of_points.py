import random
from abc import ABC, abstractmethod

import numpy as np


class NumbersOfPoints(ABC):

    def __init__(self, number_of_points: int, deviation: int):
        self.number_of_points = number_of_points
        self.deviation = deviation

    @abstractmethod
    def calculate_number_of_points(self):
        pass

class UniformPointGenerator(NumbersOfPoints):
    def calculate_number_of_points(self) -> int:
        start = self.number_of_points - self.deviation
        end = self.number_of_points + self.deviation
        return random.randint(start, end)

class NormalPointGenerator(NumbersOfPoints):
    def calculate_number_of_points(self) -> int:
        sample = np.random.normal(loc=self.number_of_points, scale=self.deviation)
        return max(1, int(round(sample)))