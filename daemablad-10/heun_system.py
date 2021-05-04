import numpy as np
from collections import namedtuple

Result = namedtuple("Result", ("x", "y"))


def heun(dy, x0, y0, h, target):
    x = x0
    y = y0

    yield Result(x=x, y=y)

    while all(x < target):
        y = y + h / 2 * (
            dy(x, y) + dy(x + h, y + h * dy(x, y))
        )
        x = x + h
        yield Result(x=x, y=y)


if __name__ == "__main__":
    # dy = lambda t, y: 2 * (t + 1) * y

    dy = lambda t, y: np.array(
        [y[1], 2 * t * y[1] - 2 * y[0]]
    )

    print("\n ====== Heun ====== \n")

    for x, y in heun(
        dy,
        np.array([0, 0]).T,
        np.array([1, 1]).T,
        np.array([0.25, 0.25]).T,
        4,
    ):
        print(f"({x}, {y})")
