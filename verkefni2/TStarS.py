import numpy as np
from scipy.optimize import bisect, newton
from AdaptiveQuadrature import adaptive_quad_length_T


def optimization_function(t, s, f, simpson=False):
    return s - adaptive_quad_length_T(
        t, f, simpson=simpson
    ) / adaptive_quad_length_T(1, f, simpson=simpson)


def find_t_for_s(s, f, simpson=True):
    return bisect(
        lambda t: optimization_function(
            t, s, f, simpson=simpson
        ),
        -1 + 0.01,
        1.1,
    )


def find_t_for_s_newton(s, f, h=0.0001, simpson=True):
    # Three-point centered-difference (5.7)
    def optimization_prime(t):
        return (
            optimization_function(
                t + h, s, f, simpson=simpson
            )
            - optimization_function(
                t - h, s, f, simpson=simpson
            )
        ) / (2 * h)

    # Tried using s as initial guess but got strange errors
    # Use s as initial guess if derivative at s isn't zero
    # if np.abs(optimization_prime(s)) < 0.01:
    #     if s > 0.5:
    #         s += 1
    #     else:
    #         s -= 1

    try:
        # Using 0.6 as initial guess
        return newton(
            lambda t: optimization_function(
                t, s, f, simpson=simpson
            ),
            0.6,
            fprime=optimization_prime,
        )
    except:
        # TODO: Figure this out???
        print(f"Failed for {s}")
        pass


if __name__ == "__main__":
    import time
    import random
    from Definitions import f

    def get_avg_time(repeats, function):
        start_time = time.perf_counter()
        for _ in range(repeats):
            function()
        return (time.perf_counter() - start_time) / repeats

    # Find t so that length from 0 to t = 0.5
    t_bisect = find_t_for_s(1 / 2, f, simpson=False)
    t_bisect_simpson = find_t_for_s(1 / 2, f)
    t_newton = find_t_for_s(1 / 2, f, simpson=False)
    t_newton_simpson = find_t_for_s(1 / 2, f)
    print("Bisect:          ", t_bisect)
    print("Bisect simpson:  ", t_bisect_simpson)
    print("Newton:          ", t_newton)
    print("Newton simpson:  ", t_newton_simpson)

    bisect_time = get_avg_time(
        1000,
        lambda: find_t_for_s(
            random.random(), f, simpson=False
        ),
    )
    bisect_simpson_time = get_avg_time(
        1000, lambda: find_t_for_s(random.random(), f)
    )
    newton_time = get_avg_time(
        1000,
        lambda: find_t_for_s_newton(
            random.random(), f, simpson=False
        ),
    )
    newton_simpson_time = get_avg_time(
        1000,
        lambda: find_t_for_s_newton(random.random(), f),
    )

    print("Bisect time:          ", bisect_time)
    print("Bisect simpson time:  ", bisect_simpson_time)
    print("Newton time:          ", newton_time)
    print("Newton simpson time:  ", newton_simpson_time)
