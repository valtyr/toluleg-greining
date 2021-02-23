import numpy as np
from numpy.linalg import solve
import pprint


class f1:
    @staticmethod
    def f(u, v):
        return u ** 3 - v ** 3 + u

    @staticmethod
    def du(u, v):
        return 3 * u ** 2 + 1

    @staticmethod
    def dv(u, v):
        return 3 * v ** 2


class f2:
    @staticmethod
    def f(u, v):
        return u ** 2 + v ** 2

    @staticmethod
    def du(u, v):
        return 2 * u

    @staticmethod
    def dv(u, v):
        return 2 * v


def f(u, v):
    return np.matrix([[f1.f(u, v)], [f2.f(u, v)]])


def jacobian(u, v):
    return np.matrix(
        [
            [f1.du(u, v), f1.dv(u, v)],
            [f2.du(u, v), f2.dv(u, v)],
        ]
    )


def newton(function, jacobian, guess, steps=10):
    history = [np.array(guess)]
    x_last = np.array(guess)

    n = len(guess)

    for _ in range(steps):
        solution = solve(
            jacobian(*x_last), -1 * function(*x_last)
        )
        x_last = x_last + np.asarray(solution).T[0]

        history.append(x_last)

    return x_last, history


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    solution, history = newton(f, jacobian, (1, 1), 10)

    pp.pprint(history)
