---
documentclass: homework
classoption:
- 11pt
- largemargins
- papersize:a4
newtxmathoptions:
- cmintegrals
- cmbraces
colorlinks: true
linkcolor: RoyalBlue
urlcolor: RoyalBlue
header-includes:
- '\usepackage[icelandic]{babel}'
- '\usepackage{commath}'
- '\newcommand{\hwname}{Valtýr Örn Kjartansson}'
- '\newcommand{\hwemail}{vok4}'
- '\newcommand{\hwtype}{Verkefni}'
- '\newcommand{\hwnum}{1}'
- '\newcommand{\hwclass}{STÆ405G}'
- '\newcommand{\hwlecture}{}'
- '\newcommand{\hwsection}{}'
---

\maketitle

# Problem {-}



```{.py include=verkefni-1/f.py snippet=f}
```

```


$ python3 f.py

0
0

```

# Problem {-}

```{#f-plot .matplotlib format=PDF caption="Mynd af f"}

import sys
sys.path.insert(1, './verkefni-1')

from f import plot

plot()

```

# Problem {-}

```{#image-recreation .matplotlib format=PDF caption="Endurgerð af mynd 1.15"}

import sys
import numpy as np
sys.path.insert(1, './verkefni-1')

from f import StewartPlatform

system = StewartPlatform()
system.draw(-np.pi / 4, np.pi / 4)

```


# Problem {-}

```{#image-recreation .matplotlib format=PDF caption="Endurgerð af mynd 1.15"}

import sys
import numpy as np
from scipy import optimize

sys.path.insert(1, './verkefni-1')

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
    p2=5,
    p3=3,
)

root_1 = optimize.bisect(system.f, -1, -0.5)
root_2 = optimize.bisect(system.f, -0.5, 0)
root_3 = optimize.bisect(system.f, 1, 1.5)
root_4 = optimize.bisect(system.f, 2, 2.3)

system.plot(
    points=[
        {
            "x": root_1,
            "label": f"$R_1 = {root_1}$",
            "symbol": "*",
        },
        {
            "x": root_2,
            "label": f"$R_2 = {root_2}$",
            "symbol": "*",
        },
        {
            "x": root_3,
            "label": f"$R_3 = {root_3}$",
            "symbol": "*",
        },
        {
            "x": root_4,
            "label": f"$R_4 = {root_4}$",
            "symbol": "*",
        },
    ]
)

```



```{#image-recreation .matplotlib format=PDF caption="Endurgerð af mynd 1.15"}

import sys
import numpy as np
from scipy import optimize

sys.path.insert(1, './verkefni-1')

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
    p2=5,
    p3=3,
)

root_1 = optimize.bisect(system.f, -1, -0.5)
root_2 = optimize.bisect(system.f, -0.5, 0)
root_3 = optimize.bisect(system.f, 1, 1.5)
root_4 = optimize.bisect(system.f, 2, 2.3)

system.draw(root_1, root_2, root_3, root_4, rows=2)

```
