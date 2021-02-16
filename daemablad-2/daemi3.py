import numpy as np


def secant(f, x1, x2, iterations=2):
    for _ in range(iterations):
        xn = x2 - (f(x2) * (x2 - x1)) / (f(x2) - f(x1))
        x1 = x2
        x2 = xn
    return x2


def false_position(f, a, b, iterations=2):
    if f(a) * f(b) >= 0:
        raise ValueError(
            "f(a) and f(b) should have different signs"
        )

    c = 0
    for _ in range(iterations):
        c = (b * f(a) - a * f(b)) / (f(a) - f(b))

        if f(c) == 0:
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c


def iqi(f, a, b, c, iterations=2):
    x1 = a
    x2 = b
    x3 = c

    for _ in range(iterations):
        q = f(x1) / f(x2)
        r = f(x3) / f(x2)
        s = f(x3) / f(x1)

        xn = x3 - (
            (
                r * (r - q) * (x3 - x2)
                + (1 - r) * s * (x3 - x1)
            )
            / ((q - 1) * (r - 1) * (s - 1))
        )
        x1 = x2
        x2 = x3
        x3 = xn

    return x3


def f(x):
    return np.exp(x) + np.sin(x) - 4


print("Secant:         ", secant(f, 1, 2))
print("False position: ", false_position(f, 1, 2))
print("IQI:            ", iqi(f, 1, 2, 0))
