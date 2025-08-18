import math
import random


def poisson_sampling(width, height, r, k=30):

    """
    r – minimalna odległość między punktami (np. minimalny odstęp między jądrami komórkowymi).
    k – maksymalna liczba prób dodania nowego punktu wokół istniejącego (najczęściej k=30).
    W, H – rozmiar obszaru (np. obrazka, na którym generujesz jądra).
    """
    points = []
    cell_size = r / math.sqrt(2)

    cols = int(width / cell_size) + 1
    rows = int(height / cell_size) + 1

    grid = [[None for _ in range(rows)] for _ in range(cols)]

    x = random.uniform(0,width)
    y = random.uniform(0,height)
    p0 = (x,y)

    points.append(p0)

    grid_x = int(x // cell_size)
    grid_y = int(y // cell_size)
    grid[grid_x][grid_y] = p0

    return points, grid


