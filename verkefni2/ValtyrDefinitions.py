import numpy as np

import matplotlib.pyplot as plt
from Bezier import Bezier


class Bezier:
    def __init__(self, points):
        (
            (x1, y1, _),
            (x2, y2, _),
            (x3, y3, _),
            (x4, y4, _),
        ) = points
        self.points = points

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

        self._bx = 3 * (x2 - x1)
        self._cx = 3 * (x3 - x2) - self._bx
        self._dx = x4 - x1 - self._bx - self._cx
        self._by = 3 * (y2 - y1)
        self._cy = 3 * (y3 - y2) - self._by
        self._dy = y4 - y1 - self._by - self._cy

    def x(self, t):
        return (
            self.x1
            + self._bx * t
            + self._cx * t ** 2
            + self._dx * t ** 3
        )

    def y(self, t):
        return (
            self.y1
            + self._by * t
            + self._cy * t ** 2
            + self._dy * t ** 3
        )

    def dx(self, t):
        return (
            self._bx
            + 2 * self._cx * t
            + 3 * self._dx * t ** 2
        )

    def dy(self, t):
        return (
            self._by
            + 2 * self._cy * t
            + 3 * self._dy * t ** 2
        )

    def f(self, t):
        return np.sqrt(self.dx(t) ** 2 + self.dy(t) ** 2)


curve = Bezier(
    [(0, 0, 0), (2, 2, 0), (-1, 2, 0), (1, 0, 0)]
)
