from heun import Result


def runge_kutta_4(dy, x0, y0, h, target):
    x = x0
    y = y0

    yield Result(x=x, y=y)

    while x < target:
        s1 = dy(x, y)
        s2 = dy(x + h / 2, y + h / 2 * s1)
        s3 = dy(x + h / 2, y + h / 2 * s2)
        s4 = dy(x + h, y + h * s3)

        y = y + h / 6 * (s1 + 2 * s2 + 2 * s3 + s4)
        x = x + h

        yield Result(x=x, y=y)


if __name__ == "__main__":
    dy = lambda t, y: 5 * t ** 4 * y

    print("\n ====== RK4 ====== \n")

    for x, y in runge_kutta_4(dy, 0, 1, 0.25, 1):
        print(f"({x}, {y})")
