import random

def ellipse_proportion(x):
    ratio = 0.65
    y = x * 0.65
    return (int(x), int(y))

def elipse_axis_dimension_generator(od = 10  , do = 100):
    dimension = random.randint(od, do)
    return dimension

# def