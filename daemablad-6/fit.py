import numpy as np
import matplotlib.pyplot as plt

data = np.array([(-2, 1), (0, 2), (1, 2), (2, 5)])


def fit(data):
    n, m = data.shape
    A = np.ones((n, 2))
    A[:, -1] = data[:, 0]
    b = np.array(
        [[np.log(v)] for v in data[:, -1].flatten()]
    )
    x = np.matmul(
        np.matmul(np.linalg.inv(np.matmul(A.T, A)), A.T), b
    )

    def error_function(t, y):
        return np.exp(x[0, 0]) * np.exp(x[1, 0] * t) - y

    return x, error_function


def plot(data, x):
    plt.style.use(
        "https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pacoty.mplstyle"
    )

    t = np.linspace(-3, 3, 100)
    y = np.exp(x[0, 0]) * np.exp(x[1, 0] * t)
    plt.plot(t, y)

    for point in data:
        plt.plot(*point, "o")

    plt.show()


def calculate_error(data, error_function):
    return [error_function(*point) for point in data]
