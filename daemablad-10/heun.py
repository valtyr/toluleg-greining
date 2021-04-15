from collections import namedtuple

Result = namedtuple("Result", ("x", "y"))


def heun(dy, x0, y0, h, target):
    x = x0
    y = y0

    yield Result(x=x, y=y)

    while x < target:
        y = y + h / 2 * (
            dy(x, y) + dy(x + h, y + h * dy(x, y))
        )
        x = x + h
        yield Result(x=x, y=y)


if __name__ == "__main__":
    dy = lambda t, y: 2 * (t + 1) * y

    print("\n ====== Heun ====== \n")

    for x, y in heun(dy, 0, 1, 0.25, 4):
        print(f"({x}, {y})")
