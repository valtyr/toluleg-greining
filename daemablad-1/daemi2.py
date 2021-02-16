import numpy as np
from daemi1 import nest

x = 1.00001
a = nest(99, np.ones(100), -x, np.zeros(99))
b = (np.power(-x, 100) - 1) / (-x - 1)
print(a - b)
