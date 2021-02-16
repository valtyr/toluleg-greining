import numpy as np
from typing import Literal


METHODS = Literal["jacobi", "gauss-seidel", "sor"]


def solve(method: METHODS, A, b, s: int):
    n, m = A.shape
    w = 1.1

    if n != m or n != len(b):
        raise ArithmeticError(
            "A must be square and be as tall as b is long"
        )

    x_old = np.zeros(n)
    x_new = np.copy(x_old)

    for k in range(s):
        for i in range(n):
            x_new[i] = b[i]
            for j in range(n):
                if j != i:
                    if method == "jacobi":
                        x_new[i] = (
                            x_new[i] - A[i, j] * x_old[j]
                        )

                    if (
                        method == "gauss-seidel"
                        or method == "sor"
                    ):
                        x_new[i] = (
                            x_new[i] - A[i, j] * x_new[j]
                        )
            x_new[i] = x_new[i] / A[i, i]
            if method == "sor":
                x_new[i] = (1 - w) * x_old[i] + w * x_new[i]
        x_old = np.copy(x_new)

    return x_new


A = np.matrix(
    [
        [3, -1, 0, 0, 0, 0.5],
        [-1, 3, -1, 0, 0.5, 0],
        [0, -1, 3, -1, 0, 0],
        [0, 0, -1, 3, -1, 0],
        [0, 0.5, 0, -1, 3, -1],
        [0.5, 0, 0, 0, -1, 3],
    ]
)
b = np.array([5 / 2, 3 / 2, 1, 1, 3 / 2, 5 / 2])
solution = np.array([1, 1, 1, 1, 1, 1])

if __name__ == "__main__":
    print(solve("jacobi", A, b, 6))
    print(solve("gauss-seidel", A, b, 6))
    print(solve("sor", A, b, 6))
