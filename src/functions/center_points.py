import random
from abc import ABC, abstractmethod

from rpds.rpds import List

from functions.poisson_sampling import poisson_sampling


class CenterGenerator(ABC):

    def __init__(self, size_x, size_y, number_of_points):
        self.size_x = size_x
        self.size_y = size_y
        self.number_of_points = number_of_points
        self._points = []
        self._counter = 0

        @abstractmethod
        def generate_points(self) -> List[int,int]:
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

class PoissonAlgorithm(CenterGenerator):
    def __init__(self, size_x, size_y, radius=5, k=30):
        super().__init__(size_x,size_y)
        self.radius = radius
        self.k = k

    def generate_points(self):
        return poisson_sampling(self.size_x, self.size_y, self.radius, self.k)

class RandomAlignmentOfCenters(CenterGenerator):
    def __init__(self, size_x, size_y, number_of_points, cell_size):
        super().__init__(size_x, size_y, number_of_points )
        self.cell_size = cell_size

    def generate_points(self):
        points = []
        for _ in range(self.number_of_points):
            x = random.uniform(4 + self.cell_size, self.size_x - self.cell_size - 4)
            y = random.uniform(4 + self.cell_size, self.size_y - self.cell_size - 4)
            p = [int(x), int(y)]
            points.append(p)

        return points

class GaussianAlgorithm(CenterGenerator):
    def __init__(self, size_x, size_y, number_of_points, dev):
        super().__init__(size_x, size_y, number_of_points)
        self.dev = dev

        def generate_points(self):
            points = []
            center_x = self.size_x / 2
            center_y = self.size_y / 2

            for _ in range(self.number_of_points):
                x = random.gauss(center_x, self.size_x * self.dev)
                y = random.gauss(center_y, self.size_y * self.dev)

                x = max(0, min(int(x), self.size_x))
                y = max(0, min(int(y), self.size_y))

                points.append([x, y])

            return points


class ClusteredAlgorithm(CenterGenerator):
    """

    """

    def __init__(self, size_x, size_y, number_of_points, num_clusters = None, dev=40):
        super().__init__(size_x, size_y, number_of_points)
        self.num_clusters = num_clusters
        self.dev = dev

        if num_clusters is None:
            self.num_clusters = random.randint(3, 9)

    def generate_points(self):
        points = []

        cluster_centers = []
        for _ in range(self.num_clusters):
            cx = random.uniform(self.dev, self.size_x - self.dev)
            cy = random.uniform(self.dev, self.size_y - self.dev)
            cluster_centers.append((cx, cy))

        for _ in range(self.number_of_points):
            chosen_center = random.choice(cluster_centers)

            x = random.gauss(chosen_center[0], self.dev)
            y = random.gauss(chosen_center[1], self.dev)

            x = max(0, min(int(x), self.size_x))
            y = max(0, min(int(y), self.size_y))

            points.append([x, y])

        return points