import numpy as np

from daemi2_1 import gaussian_elimination


def generate_hillbert(n):
    h = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            h[i, j] = 1 / (i + j + 1)

    return h


if __name__ == "__main__":
    print(generate_hillbert(2))
