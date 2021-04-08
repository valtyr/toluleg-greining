from collections import namedtuple

Result = namedtuple("Result", ("x", "y"))


def euler(dy, x0, y0, h, target):
    x = x0
    y = y0

    yield Result(x=x, y=y)

    while x < target:
        y = dy(x, y) * h + y
        x = x + h
        yield Result(x=x, y=y)


if __name__ == "__main__":
    for x, y in euler(
        lambda t, y: 2 * (t + 1) * y, 0, 1, 0.25, 4
    ):
        print(f"({x}, {y})")
