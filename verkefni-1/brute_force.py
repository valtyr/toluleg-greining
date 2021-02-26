import numpy as np
from multiprocessing import Pool
from helpers import find_zero_crossings_for_p2

def brute_force_ranges(lower_bound=1, upper_bound=1000, n=5):
    test_points = np.linspace(lower_bound, upper_bound, n)

    with Pool(5) as p:
        return p.map(find_zero_crossings_for_p2, test_points)