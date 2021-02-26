import sys
import numpy as np
from scipy import optimize

from f import StewartPlatform

system = StewartPlatform(
    x1=5,
    x2=0,
    y2=6,
    L1=3,
    L2=3 * np.sqrt(2),
    L3=3,
    gamma=np.pi / 4,
    p1=5,
    p2=7,
    p3=3,
)

system.plot()

# root_1 = optimize.bisect(system.f, -1, -0.5)
# root_2 = optimize.bisect(system.f, -0.5, 0)
# root_3 = optimize.bisect(system.f, 1, 1.5)
# root_4 = optimize.bisect(system.f, 2, 2.3)

# system.draw(root_1, root_2, root_3, root_4, rows=2)