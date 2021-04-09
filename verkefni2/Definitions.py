import numpy as np

import matplotlib.pyplot as plt
from Bezier import Bezier

points = np.array([(0.5, 1.5), (0.6, 1.6), (2, 2), (0, 0)])


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


def draw_curve(fig, ax):
    t_points = np.arange(0, 1, 0.01)
    curve = Bezier.Curve(t_points, points)
    ax.plot(
        curve[:, 0],  # x-coordinates.
        curve[:, 1],  # y-coordinates.
    )


def draw_t(fig, ax, t):
    plt.plot(x(t), y(t), "ro")


if __name__ == "__main__":
    fig, ax = plt.subplots()
    draw_curve(fig, ax)
    plt.show()
