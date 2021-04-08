from AdaptiveQuadrature import adaptive_quad_length_T
from scipy.optimize import bisect


def optimization_function(t, s, f):
    return s - adaptive_quad_length_T(
        t, f
    ) / adaptive_quad_length_T(1, f)


def find_t_for_s(s, f):
    return bisect(
        lambda t: optimization_function(t, s, f),
        0 + 0.00001,
        1,
    )


if __name__ == "__main__":
    from Definitions import f

    # Find t so that length from 0 to t = 0.5
    t = find_t_for_s(1 / 2, f)
    print(t)
