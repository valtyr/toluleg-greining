from manimlib import (
    Axes,
    Circle,
    Line,
    ShowCreation,
    Scene,
    Write,
    always_redraw,
    MoveAlongPath,
    Animation,
    Uncreate,
    VGroup,
    TexText,
    FadeIn,
    RIGHT,
    UP,
    ApplyMethod,
    DashedVMobject,
)
from manimlib.utils.rate_functions import linear
import numpy as np

import sys
import os

sys.path.append(os.getcwd())


from ValtyrDefinitions import curve
from Equipartition import equipartition
from TStarS import find_t_for_s


class MoveAlongPathEquipartitioned(Animation):
    def __init__(self, mobject, axes, **kwargs):
        self.axes = axes
        super().__init__(mobject, **kwargs)

    def interpolate_mobject(self, alpha):
        t = find_t_for_s(alpha, curve.f)
        point = self.axes.coords_to_point(
            curve.x(t), curve.y(t), 0
        )
        self.mobject.move_to(point)


def Point(color):
    circle1 = Circle()
    circle1.set_width(0.2)
    circle1.set_color(color)
    circle1.set_fill(color)
    return circle1


class MyBalls(Scene):
    def construct(self):
        axes = Axes(
            (-1, 2),
            (-1, 2),
        )
        axes.add_coordinate_labels()

        point_1 = Point("#a6a6a6")
        point_2 = Point("#BC4B51")
        point_3 = Point("#0A2463")
        point_4 = Point("#a6a6a6")

        VGroup(
            point_1,
            point_2,
            point_3,
            point_4,
        ).arrange(RIGHT, buff=1)

        self.play(
            FadeIn(
                point_1,
                UP,
                run_time=0.5,
            ),
            FadeIn(
                point_2,
                UP,
                run_time=0.7,
            ),
            FadeIn(
                point_3,
                UP,
                run_time=0.9,
            ),
            FadeIn(
                point_4,
                UP,
                run_time=1.1,
            ),
        )

        self.wait(2)

        self.play(
            ApplyMethod(
                point_1.move_to,
                axes.coords_to_point(*curve.points[0]),
            ),
            ApplyMethod(
                point_2.move_to,
                axes.coords_to_point(*curve.points[1]),
            ),
            ApplyMethod(
                point_3.move_to,
                axes.coords_to_point(*curve.points[2]),
            ),
            ApplyMethod(
                point_4.move_to,
                axes.coords_to_point(*curve.points[3]),
            ),
        )

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        line1 = DashedVMobject(
            Line(
                axes.coords_to_point(*curve.points[1]),
                axes.coords_to_point(*curve.points[0]),
            ),
            num_dashes=60,
        )
        line1.set_style(stroke_color="#a6a6a6")
        line2 = DashedVMobject(
            Line(
                axes.coords_to_point(*curve.points[2]),
                axes.coords_to_point(*curve.points[3]),
            ),
            num_dashes=61,
        )
        line2.set_style(stroke_color="#a6a6a6")

        path = axes.get_parametric_curve(
            lambda t: np.array([curve.x(t), curve.y(t), 0]),
            color="#ffc387",
        )
        self.play(
            Write(line1, lag_ratio=0.01, run_time=1),
            Write(line2, lag_ratio=0.01, run_time=1),
            ShowCreation(path),
        )

        self.wait()

        self.play(
            Uncreate(point_1),
            Uncreate(point_2),
            Uncreate(point_3),
            Uncreate(point_4),
            Uncreate(line1),
            Uncreate(line2),
        )

        # Parametric animation

        n_partitions = 500

        circle1 = Circle()
        circle1.set_width(0.1)
        circle1.set_color("#69D1C5")
        self.add(circle1)

        circle2 = Circle()
        circle2.set_width(0.1)
        circle2.set_color("#E4D9FF")
        self.add(circle1)

        circle1.move_to(
            axes.coords_to_point(curve.x(0), curve.y(0), 0)
        )
        circle2.move_to(
            axes.coords_to_point(curve.x(0), curve.y(0), 0)
        )

        self.play(Write(circle1))
        self.play(Write(circle2))

        for _ in range(3):
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
                    rate_func=linear,
                ),
            )

        self.wait(2)

        self.play(
            Uncreate(axes),
            Uncreate(path),
            Uncreate(circle1),
            Uncreate(circle2),
        )
