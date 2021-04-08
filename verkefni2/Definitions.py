import numpy as np


def x(t):
    return 0.5 + 0.3 * t + 3.9 * (t ** 2) - 4.7 * (t ** 3)


def y(t):
    return 1.5 + 0.3 * t + 0.9 * (t ** 2) - 2.7 * (t ** 3)


def dx(t):
    return 0.3 + (2 * 3.9) * t - (3 * 4.7) * (t ** 2)


def dy(t):
    return 0.3 + (2 * 0.9) * t - (3 * 2.7) * (t ** 2)


def f(t):
    return np.sqrt(dx(t) ** 2 + dy(t) ** 2)
