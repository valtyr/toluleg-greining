import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as linalg
from itertools import tee

a = [(0, 3), (1, 5), (2, 4), (3, 1)]
b = [(-1, 3), (0, 5), (3, 1), (4, 1), (5, 1)]


def latex_matrix(m):
    body = " \\\\\n".join(
        [" & ".join([str(v) for v in row]) for row in m]
    )
    return f"$\\begin{{bmatrix}}\n{body}\n\\end{{bmatrix}}$"


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def natural_cubic_spline(points):
    plt.style.use(
        "https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pacoty.mplstyle"
    )
    n = len(points)
    # v1 = 0
    # vn = 0

    A = np.zeros((n, n))
    r = np.zeros((n, 1))

    delta = [
        (x - x0, y - y0)
        for ((x0, y0), (x, y)) in pairwise(points)
    ]

    for i in range(1, n - 1):
        dx0, dy0 = delta[i - 1]
        dx, dy = delta[i]

        A[i, i - 1 : i + 2] = [dx0, 2 * (dx0 + dx), dx]
        r[i] = 3 * (dy / dx - dy0 / dx0)

    # Natural cubic spline
    # endpoint conditions
    A[0, 0] = 1
    A[n - 1, n - 1] = 1

    coeff = np.zeros((n, 3))
    coeff[:, 1] = linalg.solve(A, r)[:, 0]

    for i in range(n - 1):
        dx, dy = delta[i]

        coeff[i, 2] = (coeff[i + 1, 1] - coeff[i, 1]) / (
            3 * dx
        )
        coeff[i, 0] = (
            dy / dx
            - dx * (2 * coeff[i, 1] + coeff[i + 1, 1]) / 3
        )

    return coeff[0 : n - 1, 0:3]


def cubic_spline_plot(points, k):
    n = len(points)
    coeff = natural_cubic_spline(points)

    for i in range(n - 1):
        a = points[i][1]
        b = coeff[i, 0]
        c = coeff[i, 1]
        d = coeff[i, 2]
        xi = points[i][0]
        dx = points[i + 1][0] - points[i][0]
        xs = np.linspace(
            points[i][0], points[i + 1][0], dx * k
        )
        ys = np.array(
            [
                (
                    a
                    + b * (xs - xi)
                    + c * (xs - xi) ** 2
                    + d * (xs - xi) ** 3
                )
            ]
        )
        ys = ys.T
        plt.plot(xs, ys)

    for (x, y) in points:
        plt.plot(x, y, "o", markersize=5)

    plt.show()
