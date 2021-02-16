import numpy as np


def nest(d, c, x, b):
    y = c[d]
    for i in reversed(range(d)):
        y = y * (x - b[i]) + c[i]
    return y


if __name__ == '__main__':
    x = 1.00001
    a = nest(50, np.ones(51), x, np.zeros(50))
    b = (np.power(x, 51) - 1) / (x - 1)

    print(a - b)
