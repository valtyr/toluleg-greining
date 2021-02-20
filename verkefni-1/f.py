import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt


def f(theta):
    L1 = 2
    L2 = np.sqrt(2)
    L3 = np.sqrt(2)
    gamma = np.pi / 2
    p1 = np.sqrt(5)
    p2 = np.sqrt(5)
    p3 = np.sqrt(5)

    x1 = 4
    x2 = 0
    y2 = 4

    A2 = L3 * np.cos(theta) - x1
    B2 = L3 * np.sin(theta)
    A3 = L2 * np.cos(theta + gamma) - x2
    B3 = L2 * np.sin(theta + gamma) - y2

    N1 = B3 * (
        p2 ** 2 - p1 ** 2 - A2 ** 2 - B2 ** 2
    ) - B2 * (p3 ** 2 - p1 ** 2 - A3 ** 2 - B3 ** 2)
    N2 = -A3 * (
        p2 ** 2 - p1 ** 2 - A2 ** 2 - B2 ** 2
    ) + A2 * (p3 ** 2 - p1 ** 2 - A3 ** 2 - B3 ** 2)
    D = 2 * (A2 * B3 - B2 * A3)

    return N1 ** 2 + N2 ** 2 - p1 ** 2 * D ** 2


if __name__ == "__main__":
    plt.style.use(
        "https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pacoty.mplstyle"
    )

    max_x = optimize.fmin(lambda x: -f(x), np.pi)
    root_1 = optimize.bisect(f, 0, 2)
    root_2 = optimize.bisect(f, 5, 6)

    x = np.linspace(0, 2 * np.pi, 1000)
    plt.plot(x, f(x))
    plt.plot(
        root_1,
        f(root_1),
        "*",
        markersize=12,
        label=f"$R_1$",
    )
    plt.plot(
        root_2,
        f(root_2),
        "*",
        markersize=12,
        label=f"$R_2$",
    )
    plt.plot(
        max_x, f(max_x), "o", markersize=12, label="max"
    )
    plt.legend()
    plt.show()
