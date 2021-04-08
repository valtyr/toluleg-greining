from euler import euler, Result


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
    dy = lambda t, y: t ** 3 / y ** 2

    print("\n ====== Euler ====== \n")

    for x, y in euler(dy, 0, 1, 0.25, 4):
        print(f"({x}, {y})")

    print("\n ====== Heun ====== \n")

    for x, y in heun(dy, 0, 1, 0.25, 4):
        print(f"({x}, {y})")
