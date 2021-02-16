import numpy as np


def LU(a):
    n, m = a.shape
    a = np.copy(a)

    if n != m:
        raise ArithmeticError("Matrix must be square")

    L = np.eye(n)

    for i in range(n - 1):
        if np.abs(a[i, i]) <= np.spacing(1):
            raise ArithmeticError(
                f"Zero pivot encountered at {i}, {i}"
            )

        for j in range(i + 1, n):
            mul = a[j, i] / a[i, i]
            L[j, i] = mul

            for k in range(i + 1, n):
                a[j, k] = a[j, k] - mul * a[i, k]

    return L, np.triu(a)


def backsub_upper(a, b):
    n, m = a.shape
    a = np.append(a, b.reshape((n, 1)), axis=1)

    if n != m:
        raise ArithmeticError("Matrix must be square")

    if n != len(b):
        raise ArithmeticError(
            "Vector b should have same amount of elements as matrix a has rows"
        )

    x = np.zeros(n)

    x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = a[i][n]

        for j in range(i + 1, n):
            x[i] = x[i] - a[i][j] * x[j]

        x[i] = x[i] / a[i][i]

    return x


def solve(a, b):
    L, U = LU(a)
    return backsub_upper(U, b)


daemi_2A = np.array([[3, 1, 2], [6, 3, 4], [3, 1, 5]])
daemi_2B = np.array([[4, 2, 0], [4, 4, 2], [2, 2, 3]])
daemi_2C = np.array(
    [
        [1, -1, 1, 2],
        [0, 2, 1, 0],
        [1, 3, 4, 4],
        [0, 2, 1, -1],
    ]
)

daemi_4A = (
    daemi_2A,
    np.array([0, 1, 3]),
)
daemi_4B = (
    daemi_2B,
    np.array([2, 4, 6]),
)


if __name__ == "__main__":
    print("LU factorize:")
    print(LU(daemi_2A))
    print(LU(daemi_2B))
    print(LU(daemi_2C))

    print("\nSolve with back substitution:")
    print(solve(daemi_4A[0], daemi_4A[1]))
    print(solve(daemi_4B[0], daemi_4B[1]))
