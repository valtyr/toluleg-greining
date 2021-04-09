from manimlib import (
    Axes,
    Circle,
    ShowCreation,
    Scene,
    Write,
    always_redraw,
    MoveAlongPath,
    Animation,
    Uncreate,
    Tex,
    DOWN,
)
from manimlib.utils.rate_functions import linear
import numpy as np

import sys
import os

sys.path.append(os.getcwd())


from Definitions import points, x, y, f
from Equipartition import equipartition
from TStarS import find_t_for_s


class MoveAlongPathEquipartitioned(Animation):
    def __init__(self, mobject, axes, **kwargs):
        self.axes = axes
        super().__init__(mobject, **kwargs)

    def interpolate_mobject(self, alpha):
        t = find_t_for_s(alpha, f)
        point = self.axes.coords_to_point(x(t), y(t), 0)
        self.mobject.move_to(point)


class TimingFunctions:
    @staticmethod
    def linear(t):
        return t

    @staticmethod
    def third_root(t):
        return t ** (1 / 3)

    @staticmethod
    def t_squared(t):
        return t ** 2

    @staticmethod
    def sin(t):
        return np.sin(t * (np.pi / 2))

    @staticmethod
    def equation(t):
        return 1 / 2 + (1 / 2) * np.sin(2 * t - 1) * (
            np.pi / 2
        )


class Balls(Scene):
    def construct(self):
        axes = Axes(
            (-1, 2),
            (-1, 2),
        )
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ration=0.01, run_time=1))

        path = axes.get_parametric_curve(
            lambda t: np.array([x(t), y(t), 0]),
            color="#ffc387",
        )
        self.play(
            ShowCreation(path),
        )

        # Parametric animation

        n_partitions = 200

        circle1_path = [
            axes.coords_to_point(x(t), y(t), 0)
            for t in np.arange(0, 1, n_partitions)
        ]
        circle2_path = [
            axes.coords_to_point(x(t), y(t), 0)
            for t in equipartition(f, n_partitions)
        ]

        circle1 = Circle()
        circle1.set_width(0.1)
        circle1.set_color("#69D1C5")
        self.add(circle1)

        circle2 = Circle()
        circle2.set_width(0.1)
        circle2.set_color("#E4D9FF")
        self.add(circle1)

        circle1.move_to(axes.coords_to_point(x(0), y(0), 0))
        circle2.move_to(axes.coords_to_point(x(0), y(0), 0))

        self.play(Write(circle1))
        self.play(Write(circle2))

        for _ in range(3):
            self.play(
                MoveAlongPath(
                    circle1,
                    path,
                    run_time=4,
                ),
                MoveAlongPathEquipartitioned(
                    circle2, axes, run_time=4
                ),
            )

        self.wait(2)

        self.play(
            Uncreate(axes),
            Uncreate(path),
            Uncreate(circle1),
            Uncreate(circle2),
        )


class TimingFunctionsScene(Scene):
    def construct(self):
        axes = Axes(
            (-1, 2),
            (-1, 2),
        )
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ration=0.01, run_time=1))

        path = axes.get_parametric_curve(
            lambda t: np.array([x(t), y(t), 0]),
            color="#ffc387",
        )
        self.play(
            ShowCreation(path),
        )

        # Parametric animation

        n_partitions = 200

        circle1_path = [
            axes.coords_to_point(x(t), y(t), 0)
            for t in np.arange(0, 1, n_partitions)
        ]
        circle2_path = [
            axes.coords_to_point(x(t), y(t), 0)
            for t in equipartition(f, n_partitions)
        ]

        circle1 = Circle()
        circle1.set_width(0.1)
        circle1.set_color("#69D1C5")
        self.add(circle1)

        circle2 = Circle()
        circle2.set_width(0.1)
        circle2.set_color("#E4D9FF")
        self.add(circle1)

        circle1.move_to(axes.coords_to_point(x(0), y(0), 0))
        circle2.move_to(axes.coords_to_point(x(0), y(0), 0))

        self.play(Write(circle1))
        self.play(Write(circle2))

        equation1 = Tex("C(s) = s^{ \\frac{1}{3} }")
        equation2 = Tex("C(s) = s^{2}")
        equation3 = Tex("C(s) = sin(s \\frac{\\pi}{2} )")
        equation4 = Tex(
            "C(s) = \\frac{1}{2} + \\frac{1}{2} sin(2s - 1) \\frac{\\pi}{2}"
        )

        animation_list = zip(
            (equation1, equation2, equation3, equation4),
            (
                TimingFunctions.third_root,
                TimingFunctions.t_squared,
                TimingFunctions.sin,
                TimingFunctions.equation,
            ),
        )

        for eq, func in animation_list:
            eq.shift(2 * DOWN)
            self.play(Write(eq))

            self.play(
                MoveAlongPath(
                    circle1,
                    path,
                    run_time=4,
                    rate_func=linear,
                ),
                MoveAlongPathEquipartitioned(
                    circle2,
                    axes,
                    run_time=4,
                    rate_func=func,
                ),
            )
            self.play(Uncreate(eq))

        self.wait(2)

        self.play(
            Uncreate(axes),
            Uncreate(path),
            Uncreate(circle1),
            Uncreate(circle2),
        )
