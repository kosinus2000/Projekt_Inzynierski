import random
from abc import ABC, abstractmethod
from functions.poisson_sampling import poisson_sampling


class CenterGenerator(ABC) :
    def __init__(self, size_x, size_y, number_of_points):
        self.size_x = size_x
        self.size_y = size_y
        self.number_of_points = number_of_points
        self._points = []
        self._counter = 0

        @abstractmethod
        def generate_points(self):
            pass

        def get_next_center(self):
            if not self._points:
                self._points = self.generate_points()

            if self._counter < len(self._points):
                center = self._points[self._counter]
                self._counter += 1
                return center
            else:
                self._counter = 0
                self._points = self.generate_points()
                return self.get_next_center()

class Poisson_algorithm(CenterGenerator):
    def __init__(self, size_x, size_y, radius=5, k=30):
        super().__init__(size_x,size_y)
        self.radius = radius
        self.k = k

    def generate_points(self):
        return poisson_sampling(self.size_x, self.size_y, self.radius, self.k)

class Random_algorithm(CenterGenerator):
    def __init__(self, size_x, size_y, number_of_points, cell_size):
        super().__init__(size_x, size_y, number_of_points )
        self.cell_size = cell_size


    def generate_points(self):
        lista = []
        for _ in range(self.number_of_points):
            x = random.uniform(4 + self.cell_size, self.size_x - self.cell_size - 4)
            y = random.uniform(4 + self.cell_size, self.size_y - self.cell_size - 4)
            p = [int(x), int(y)]
            lista.append(p)

