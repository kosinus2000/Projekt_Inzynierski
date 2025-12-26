import math
import random


def poisson_sampling(width, height, r = 5, k=30):
    """
    Generates a set of points following the Poisson disk sampling algorithm within the specified dimensions.
    This method ensures that no two points are closer than a given minimum radius 'r', offering a uniform
    random distribution suitable for various computational and visual applications, such as texture generation
    or spatial data sampling.

    Parameters:
        width (int or float): The width of the area to be sampled.
        height (int or float): The height of the area to be sampled.
        r (float): The minimum distance required between generated points.
        k (int, optional): The number of attempts to generate a valid point in the vicinity of an active point.
            Default is 30.

    Returns:
        list[tuple[float, float]]: A list of tuples representing the (x, y) coordinates of the generated points.

    Raises:
        ValueError: If the given width, height, or radius (`r`) are invalid or negative.
    """


    #    r – minimalna odległość między punktami
    #    k – maksymalna liczba prób dodania nowego punktu wokół istniejącego
    #    W, H – rozmiar obszaru


    points = []
    active_list = []
    cell_size = r / math.sqrt(2)

    cols = int(width / cell_size) + 1
    rows = int(height / cell_size) + 1

    grid = [[None for x in range(rows)] for x in range(cols)]

    x = random.uniform(0, width)
    y = random.uniform(0, height)
    p0 = (x, y)

    points.append(p0)
    active_list.append(p0)

    grid_x = int(x // cell_size)
    grid_y = int(y // cell_size)

    if 0 <= grid_x < cols and 0 <= grid_y < rows:
        grid[grid_x][grid_y] = p0

    while active_list:
        idx = random.randint(0, len(active_list) - 1)
        px, py = active_list[idx]
        flag = False

        for _ in range(k):
            d = r * (1 + random.random())
            angle = (2 * math.pi) * random.random()
            nx = px + d * math.cos(angle)
            ny = py + d * math.sin(angle)

            if not (0 <= nx < width and 0 <= ny < height):
                continue

            grid_x = int(nx // cell_size)
            grid_y = int(ny // cell_size)

            ok = True
            for i in range(max(0, grid_x - 1), min(cols, grid_x + 2)):
                for j in range(max(0, grid_y - 1), min(rows, grid_y + 2)):
                    col_next_to = grid[i][j]
                    if col_next_to is not None:
                        qx, qy = col_next_to
                        if math.dist((nx, ny), (qx, qy)) < r:
                            ok = False
                            break
                    if not ok:
                        break

            if ok:
                new_point = (nx, ny)
                points.append(new_point)
                active_list.append(new_point)
                grid[grid_x][grid_y] = new_point
                flag = True
                break
        if not flag:
            active_list.pop(idx)

    return points