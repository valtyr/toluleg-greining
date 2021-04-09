import matplotlib.pyplot as plt

from TStarS import find_t_for_s_newton
from Definitions import draw_curve, draw_t


def equipartition(f, n):
    length = 1 / n
    return [
        find_t_for_s_newton(length * i, f, simpson=False)
        for i in range(1, n + 1)
    ]


def draw_partitions(partitions):
    fig, ax = plt.subplots()
    draw_curve(fig, ax)

    for t in partitions:
        draw_t(fig, ax, t)

    plt.show()


if __name__ == "__main__":
    from Definitions import f

    partitions_4 = equipartition(f, 4)
    partitions_20 = equipartition(f, 20)

    print(partitions_4)
    draw_partitions(partitions_4)

    print(partitions_20)
    draw_partitions(partitions_20)
