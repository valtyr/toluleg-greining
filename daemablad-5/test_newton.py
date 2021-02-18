import numpy as np
from newton2 import newton


def jacobian(x):
    u, v = x
    return np.array([
        [3**u**2 + 1, 3*v**2],
        [2*u, 2*v]
        ])

def f(x):
    u, v = x
    return np.array([
        [u**3 - v**3 + u],
        [u**2 + v**2]
        ])

newton(f, jacobian, np.array([2, -1]), eps=0.0001)
