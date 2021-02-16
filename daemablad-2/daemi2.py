import numpy as np


def fixed_point_it(f, r, x0, tol=1e-5):
    xn = x0
    i = 0

    while np.abs(r - xn) > tol:
        xn = f(xn)

        i += 1
        if i > 1e6:
            return None

    return i


def f1(x):
    return 0.5 * x + 1 / x


def f2(x):
    return 2 / 3 * x + 2 / (3 * x)


def f3(x):
    return 3 / 4 * x + 1 / (2 * x)


print("A: ", fixed_point_it(f1, np.sqrt(2), 1))
print("B: ", fixed_point_it(f2, np.sqrt(2), 1))
print("C: ", fixed_point_it(f3, np.sqrt(2), 1))
