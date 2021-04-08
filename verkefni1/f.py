# start snippet f
import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections as mc
from collections import namedtuple


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


# end snippet f

Point = namedtuple("Point", ("x", "y"))


class StewartPlatform:
    def __init__(
        self,
        L1=2,
        L2=np.sqrt(2),
        L3=np.sqrt(2),
        gamma=np.pi / 2,
        p1=np.sqrt(5),
        p2=np.sqrt(5),
        p3=np.sqrt(5),
        x1=4,
        x2=0,
        y2=4,
    ):
        self.L1 = L1
        self.L2 = L2
        self.L3 = L3
        self.gamma = gamma
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.x1 = x1
        self.x2 = x2
        self.y2 = y2

    def f(self, theta):
        A2 = self.L3 * np.cos(theta) - self.x1
        B2 = self.L3 * np.sin(theta)
        A3 = self.L2 * np.cos(theta + self.gamma) - self.x2
        B3 = self.L2 * np.sin(theta + self.gamma) - self.y2

        N1 = B3 * (
            self.p2 ** 2 - self.p1 ** 2 - A2 ** 2 - B2 ** 2
        ) - B2 * (
            self.p3 ** 2 - self.p1 ** 2 - A3 ** 2 - B3 ** 2
        )
        N2 = -A3 * (
            self.p2 ** 2 - self.p1 ** 2 - A2 ** 2 - B2 ** 2
        ) + A2 * (
            self.p3 ** 2 - self.p1 ** 2 - A3 ** 2 - B3 ** 2
        )
        D = 2 * (A2 * B3 - B2 * A3)

        return N1 ** 2 + N2 ** 2 - self.p1 ** 2 * D ** 2

    def platform(self, theta):
        A2 = self.L3 * np.cos(theta) - self.x1
        B2 = self.L3 * np.sin(theta)
        A3 = self.L2 * np.cos(theta + self.gamma) - self.x2
        B3 = self.L2 * np.sin(theta + self.gamma) - self.y2

        N1 = B3 * (
            self.p2 ** 2 - self.p1 ** 2 - A2 ** 2 - B2 ** 2
        ) - B2 * (
            self.p3 ** 2 - self.p1 ** 2 - A3 ** 2 - B3 ** 2
        )
        N2 = -A3 * (
            self.p2 ** 2 - self.p1 ** 2 - A2 ** 2 - B2 ** 2
        ) + A2 * (
            self.p3 ** 2 - self.p1 ** 2 - A3 ** 2 - B3 ** 2
        )
        D = 2 * (A2 * B3 - B2 * A3)

        x = N1 / D
        y = N2 / D

        point_1 = Point(x, y)
        point_2 = Point(
            x + self.L2 * np.cos(theta + self.gamma),
            y + self.L2 * np.sin(theta + self.gamma),
        )
        point_3 = Point(
            x + self.L3 * np.cos(theta),
            y + self.L3 * np.sin(theta),
        )

        return point_1, point_2, point_3

    def draw(self, *thetas, rows=1):
        plt.style.use(
            "https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pacoty.mplstyle"
        )
        fig, axs = plt.subplots(rows, len(thetas) // rows)

        A1, A2, A3 = (
            Point(0, 0),
            Point(self.x2, self.y2),
            Point(self.x1, 0),
        )

        try:
            axs = axs.flatten()
        except:
            pass

        for theta, ax in zip(thetas, axs):
            C1, C2, C3 = self.platform(theta)

            lines = [
                (A1, C1),
                (A2, C2),
                (A3, C3),
                (C1, C2),
                (C2, C3),
                (C3, C1),
            ]
            lines = mc.LineCollection(lines)

            ax.add_collection(lines)
            ax.set_aspect("equal", adjustable="box")

            ax.plot(*A1, "o", label="$(0,0)$")
            ax.plot(*A2, "o", label="$(x_2,y_2)$")
            ax.plot(*A3, "o", label="$(x_1,0)$")
            ax.plot(*C1, "o", label="$(x,y)$")
            ax.plot(
                *C2,
                "o",
                label="$(x + L_2 \\cos{\\theta + \\gamma},y_2 + L_2  \\sin{\\theta + \\gamma})$",
            )
            ax.plot(
                *C3,
                "o",
                label="$(x + L_3 \\cos{\\theta},y_2 + L_3  \\sin{\\theta})$",
            )

            ax.autoscale()

        x_lower = min([a.get_xlim()[0] for a in axs])
        x_upper = max([a.get_xlim()[1] for a in axs])
        y_lower = min([a.get_ylim()[0] for a in axs])
        y_upper = max([a.get_ylim()[1] for a in axs])

        for a in axs:
            a.set_xlim((x_lower, x_upper))
            a.set_ylim((y_lower, y_upper))

        plt.show()

    def plot(self, points=[]):
        plt.style.use(
            "https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pacoty.mplstyle"
        )
        x = np.linspace(-np.pi, np.pi, 1000)
        plt.plot(x, self.f(x))

        for point in points:
            plt.plot(
                point["x"],
                f(point["x"]),
                point["symbol"],
                markersize=12,
                label=point["label"],
            )

        if points:
            plt.legend()

        plt.show()


def plot():
    plt.style.use(
        "https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pacoty.mplstyle"
    )

    # f = system()

    max_x = optimize.fmin(lambda x: -f(x), np.pi)
    root_1 = optimize.bisect(f, -2, 0)
    root_2 = optimize.bisect(f, 0, 2)

    x = np.linspace(-np.pi, np.pi, 1000)
    plt.plot(x, f(x))
    plt.plot(
        root_1,
        f(root_1),
        "*",
        markersize=12,
        label="$R_1 = -\\frac{\\pi}{4}$",
    )
    plt.plot(
        root_2,
        f(root_2),
        "*",
        markersize=12,
        label="$R_2 = \\frac{\\pi}{4}$",
    )
    plt.plot(
        max_x,
        f(max_x),
        "o",
        markersize=12,
        label="$max = \\pi$",
    )

    plt.legend()
    plt.show()


if __name__ == "__main__":
    system = StewartPlatform(
        x1=5,
        x2=0,
        y2=6,
        L1=3,
        L2=3 * np.sqrt(2),
        L3=3,
        gamma=np.pi / 4,
        p1=5,
        p2=5,
        p3=3,
    )

    root_1 = optimize.bisect(system.f, -1, -0.5)
    root_2 = optimize.bisect(system.f, -0.5, 0)
    root_3 = optimize.bisect(system.f, 1, 1.5)
    root_4 = optimize.bisect(system.f, 2, 2.3)

    print(root_4)

    system.plot(
        points=[
            {
                "x": root_1,
                "label": f"$R_1 = {root_1}$",
                "symbol": "*",
            },
            {
                "x": root_2,
                "label": f"$R_2 = {root_2}$",
                "symbol": "*",
            },
            {
                "x": root_3,
                "label": f"$R_3 = {root_3}$",
                "symbol": "*",
            },
            {
                "x": root_4,
                "label": f"$R_4 = {root_4}$",
                "symbol": "*",
            },
        ]
    )

    system.draw(root_1, root_2, root_3, root_4, rows=2)
