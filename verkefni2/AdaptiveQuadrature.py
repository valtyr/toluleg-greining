import numpy as np
from itertools import tee


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def adaptive_quad_length(points, f, tolerance=0.005):
    def s(a, b):
        return (b - a) * ((f(a) + f(b)) / 2)

    def quad(a, b, a_orig, b_orig):
        c = (a + b) / 2

        s_ab = s(a, b)
        s_ac = s(a, c)
        s_cb = s(c, b)

        if s_ab - s_ac - s_cb < 3 * tolerance * (
            (b - a) / (b_orig - a_orig)
        ):
            return s_ac + s_cb
        else:
            return quad(a, c, a_orig, b_orig) + quad(
                c, b, a_orig, b_orig
            )

    return sum(
        [quad(a, b, a, b) for a, b in pairwise(points)]
    )


def adaptive_quad_length_T(
    T, f, tolerance=0.005, simpson=False
):
    def s(a, b):
        return (b - a) * ((f(a) + f(b)) / 2)

    def quad(a, b, a_orig, b_orig):
        c = (a + b) / 2

        s_ab = s(a, b)
        s_ac = s(a, c)
        s_cb = s(c, b)

        criterion = (
            np.abs(s_ab - (s_ac + s_cb)) < 10 * tolerance
            if simpson
            else s_ab - s_ac - s_cb
            < 3 * tolerance * ((b - a) / (b_orig - a_orig))
        )

        if criterion:
            return s_ac + s_cb
        else:
            return quad(a, c, a_orig, b_orig) + quad(
                c, b, a_orig, b_orig
            )

    return quad(0, T, 0, T)


if __name__ == "__main__":
    from Definitions import f

    # points = [0, 1 / 4, 1 / 2, 3 / 4]
    length = adaptive_quad_length_T(1, f)
    print(length)
