import numpy as np
from scipy import optimize


def generate_matrix(x):
    return np.array(
        [
            [1, 2, 3, x],
            [4, 5, x, 6],
            [7, x, 8, 9],
            [x, 10, 11, 12],
        ]
    )


def f(x):
    return np.linalg.det(generate_matrix(x)) - 1000


x1 = optimize.bisect(f, -100, 0)
x2 = optimize.bisect(f, 0, 100)

print("SOLUTIONS:")
print("Root x1: {}    Det(x1):  {:.15f}".format(x1, f(x1)))
print("Root x2:   {}   Det(x2): {:.15f}".format(x2, f(x2)))
