import numpy as np
from splines import latex_matrix

data = np.matrix([(4, 8, 1), (0, 2, -2), (3, 6, 7)])


def qr(A):
    m, n = A.shape

    r = np.zeros((m, n))
    q = np.zeros((n, n))

    for j in range(n):
        y = A[:, j]

        r[j, j] = np.linalg.norm(y.T)
        q[:, j] = (y / r[j, j]).flatten()

        for i in range(j - 1):
            r[j, i] = q[:, j].T * y
            y = y - r[j, i] * q[:, i]

    return q, r


if __name__ == "__main__":
    q, r = qr(data)
    print(latex_matrix(q))
    print(latex_matrix(r))
