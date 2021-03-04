import numpy as np
import matplotlib.pyplot as plt

from multiprocessing import Pool
from helpers import find_zero_crossings_for_p2

def brute_force_ranges(lower_bound=3.5, upper_bound=9.5, n=2000):
    test_points = np.linspace(lower_bound, upper_bound, n)

    with Pool(6) as p:
        return p.map(find_zero_crossings_for_p2, test_points)


def plot():
    results = brute_force_ranges()
    plt.style.use(
        "https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pacoty.mplstyle"
    )

    plt.plot([p[0] for p in results], [p[1] for p in results])
    plt.show()
    
    