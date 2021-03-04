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

Write a function for $f(\theta)$. The parameters $L_1$, $L_2$, $L_3$, $\gamma$, $x_1$, $x_2$, $y_2$ are fixed constants,
and the strut lengths $p_1$, $p_2$, $p_3$ will be known for a given pose. 

To test your code, set the parameters $L_1 = 2$, $L_2 = L_3 = \sqrt{2}$, $p_3 = 2$, $\gamma = \frac{\pi}{2}$, $p_1 = p_2 =
\sqrt{5}$ from Figure 1.15. Then, substituting $\theta = -\frac{\pi}{4}$ or $\theta = \frac{\pi}{4}$, corresponding to
Figures 1.15(a, b), respectively, should make $f(\theta) = 0$.

\answerheader{Solution:}

```{.py include=verkefni-1/f.py snippet=f}
```

```


$ python3 -i f.py

> f(np.pi / 4)
0

> f(-np.pi / 4)
0

```

\newpage

# Problem {-}

Plot $f(\theta)$ on $[-\pi, \pi]$. As a check of your work, there should be roots at $\pm\frac{\pi}{4}$.

\answerheader{Solution:}

````python
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def plot():
    max_x = optimize.fmin(lambda x: -f(x), np.pi)
    root_1 = optimize.bisect(f, -2, 0)
    root_2 = optimize.bisect(f, 0, 2)

    x = np.linspace(-np.pi, np.pi, 1000)
    plt.plot(x, f(x))
    plt.plot(
        root_1,
        f(root_1),
        "*",
        markersize=12,
        label="$R_1 = -\\frac{\\pi}{4}$",
    )
    plt.plot(
        root_2,
        f(root_2),
        "*",
        markersize=12,
        label="$R_2 = \\frac{\\pi}{4}$",
    )
    plt.plot(
        max_x,
        f(max_x),
        "o",
        markersize=12,
        label="$max = \\pi$",
    )

    plt.legend()
    plt.show()

plot()
````

```{#f-plot .matplotlib format=PDF caption="Mynd af f"}

import sys
sys.path.insert(1, './verkefni-1')

from f import plot

plot()

```

\newpage

# Problem {-}

Reproduce Figure 1.15.

\answerheader{Solution:}

Notum `StewartPlatform` klasann aftast í skjalinu. Ef engar inntaksbreytur eru gefnar upp þá lýsir klasinn
kerfi dæmisins.

````python
import numpy as np
from f import StewartPlatform

system = StewartPlatform()
system.draw(-np.pi / 4, np.pi / 4)

````

```{#image-recreation .matplotlib format=PDF caption="Endurgerð af mynd 1.15"}

import sys
import numpy as np
sys.path.insert(1, './verkefni-1')

from f import StewartPlatform

system = StewartPlatform()
system.draw(-np.pi / 4, np.pi / 4)

```


\newpage

# Problem {-}

Solve the forward kinematics problem for the planar Stewart platform specified by
$x_1=5$, $(x_2,y_2)=(0,6)$, $L_1 = L_3 = 3$, $L_2 = 3\sqrt{2}$, $\gamma= \frac{\pi}{4}$, $p_1 = p_2 = 5$, $p_3 = 3$.

Begin by plotting $f(\theta)$. Use an equation solver to find all four poses, and plot them.
Check your answers by verifying that $p_1$, $p_2$, $p_3$ are the lengths of the struts in your plot.

\answerheader{Solution:}

Notum `StewartPlatform` klasann aftast í skilunum og `optimize.bisect` úr Scipy kóðasafninu til þess
að finna rætur. Ágiskanir eru einfaldlega lesnar af mynd.

```python

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

Nú fæst [mynd](#problem-4-f) af fallinu $f(\theta)$ þar sem allar rætur merktar inn.

```{#problem-4-f .matplotlib format=PDF caption="Mynd af f"}

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

Út frá þessum gildum á $\theta$ getum við teiknað upp myndir af gildum stöðum kerfisins.

Kóðinn er einfaldur:

```python
system.draw(root_1, root_2, root_3, root_4, rows=2)
```

og út fást [4 myndir](#problem-4-dancers).



```{#problem-4-dancers .matplotlib format=PDF caption="Gildar stöður kerfis"}

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

Með því að nota horn yfirborðsins og punktana sem fæturnir eru fastir við er hægt að reikna út lengd fótanna.
Þær stemma allar við forsendur.

\newpage

# Problem {-}

Change strut length to $p_2 = 7$ and re-solve the problem. For these parameters, there are six poses.

\answerheader{Solution:}

Notum sama klasa og áður en þetta skiptið ætlum við að nota `find_zeros` aftast úr skjalinu til þess að finna allar
rætur f í einu. Fallið notar `numpy.linspace` til þess að búa til röð n talna milli $-\pi$ og $\pi$.
Fallið skoðar svo tvær samliggjandi tölur úr röðinni í einu og athugar hvort samsvarandi y-gildi hafi mismunandi formerki.
Ef svo er bætir það parinu í lista af gildum til að nota sem ágiskanir í `bisect` kall. Á endanum skilar það rótum
fallsins.


```python

import sys
import numpy as np

from f import StewartPlatform
from helpers import find_zeros

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

zeros = find_zeros(system.f)

points = [
  {
    'x': zero,
    'symbol': '*',
    'label': f'$x_{i+1} = {system.f(zero):.4e}$'
  }
  for i, zero in enumerate(zeros)
]

system.plot(points)
system.draw(*zeros, rows=int(np.sqrt(len(zeros))) or None)

```

```{.matplotlib format=PDF caption="$f(\theta)$ fyrir $p_2 = 7$"}

import sys
import numpy as np
from scipy import optimize

sys.path.insert(1, './verkefni-1')

from f import StewartPlatform
from helpers import find_zeros

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

zeros = find_zeros(system.f)

points = [{'x': zero, 'symbol': '*', 'label': f'$x_{i+1} = {system.f(zero):.4e}$'} for i, zero in enumerate(zeros)]
system.plot(points)

```

```{.matplotlib format=PDF caption="Stöður fyrir $p_2 = 7$"}

import sys
import numpy as np
from scipy import optimize

sys.path.insert(1, './verkefni-1')

from f import StewartPlatform
from helpers import find_zeros

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

zeros = find_zeros(system.f)

points = [{'x': zero, 'symbol': '*', 'label': f'$x_{i+1} = {system.f(zero):.4e}$'} for i, zero in enumerate(zeros)]
system.draw(*zeros, rows=int(np.sqrt(len(zeros))) or None)

```

\newpage

# Problem {-}

Find a strut length $p_2$, with the rest of the parameters as in Step 4, for which there are only two poses.

\answerheader{Solution:}

Dæmi 7 var unnið á undan dæmi 6 og niðurstöður notaðar. Ef við skoðum myndina þá sést að í $p_2 = 4$ eru bara 2 stöður.

```python

import sys
import numpy as np

from f import StewartPlatform
from helpers import find_zeros

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

zeros = find_zeros(system.f)

points = [
  {
    'x': zero,
    'symbol': '*',
    'label': f'$x_{i+1} = {system.f(zero):.4e}$'
  }
  for i, zero in enumerate(zeros)
]

system.draw(*zeros, rows=int(np.sqrt(len(zeros))) or None)

```

```{.matplotlib format=PDF caption="Stöður fyrir $p_2 = 4$"}

import sys
import numpy as np
from scipy import optimize

sys.path.insert(1, './verkefni-1')

from f import StewartPlatform
from helpers import find_zeros

system = StewartPlatform(
    x1=5,
    x2=0,
    y2=6,
    L1=3,
    L2=3 * np.sqrt(2),
    L3=3,
    gamma=np.pi / 4,
    p1=5,
    p2=4,
    p3=3,
)

zeros = find_zeros(system.f)

points = [{'x': zero, 'symbol': '*', 'label': f'$x_{i+1} = {system.f(zero):.4e}$'} for i, zero in enumerate(zeros)]
system.draw(*zeros, rows=int(np.sqrt(len(zeros))) or None)

```


\newpage

# Problem{-}


Calculate the intervals in $p_2$, with the rest of the parameters as in Step 4, for which there are 0, 2, 4, and 6 poses,
respectively.

\answerheader{Solution:}

Notum `find_zero_crossing_for_p2` fallið aftast í skjalinu og `multiprocessing` safnið sem er byggt inn
í python:

```python
import numpy as np
import matplotlib.pyplot as plt

from multiprocessing import Pool
from helpers import find_zero_crossings_for_p2

def brute_force_ranges(
    lower_bound=3.5,
    upper_bound=9.5,
    n=2000
):
    test_points = np.linspace(lower_bound, upper_bound, n)

    with Pool(6) as p:
        return p.map(find_zero_crossings_for_p2, test_points)


def plot():
    results = brute_force_ranges()

    plt.plot([p[0] for p in results], [p[1] for p in results])
    plt.show()

plot()
```

Út fæst [mynd](#intervals) af bilunum:

```{#intervals .matplotlib format=PDF caption="Endurgerð af mynd 1.15"}

import sys
import numpy as np
from scipy import optimize

sys.path.insert(1, './verkefni-1')

from brute_force import plot
plot()

```

\newpage

## f.py

```python
import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections as mc
from collections import namedtuple

class StewartPlatform:
    def __init__(
        self,
        L1=2,
        L2=np.sqrt(2),
        L3=np.sqrt(2),
        gamma=np.pi / 2,
        p1=np.sqrt(5),
        p2=np.sqrt(5),
        p3=np.sqrt(5),
        x1=4,
        x2=0,
        y2=4,
    ):
        self.L1 = L1
        self.L2 = L2
        self.L3 = L3
        self.gamma = gamma
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.x1 = x1
        self.x2 = x2
        self.y2 = y2

    def f(self, theta):
        A2 = self.L3 * np.cos(theta) - self.x1
        B2 = self.L3 * np.sin(theta)
        A3 = self.L2 * np.cos(theta + self.gamma) - self.x2
        B3 = self.L2 * np.sin(theta + self.gamma) - self.y2

        N1 = B3 * (
            self.p2 ** 2 - self.p1 ** 2 - A2 ** 2 - B2 ** 2
        ) - B2 * (
            self.p3 ** 2 - self.p1 ** 2 - A3 ** 2 - B3 ** 2
        )
        N2 = -A3 * (
            self.p2 ** 2 - self.p1 ** 2 - A2 ** 2 - B2 ** 2
        ) + A2 * (
            self.p3 ** 2 - self.p1 ** 2 - A3 ** 2 - B3 ** 2
        )
        D = 2 * (A2 * B3 - B2 * A3)

        return N1 ** 2 + N2 ** 2 - self.p1 ** 2 * D ** 2

    def platform(self, theta):
        A2 = self.L3 * np.cos(theta) - self.x1
        B2 = self.L3 * np.sin(theta)
        A3 = self.L2 * np.cos(theta + self.gamma) - self.x2
        B3 = self.L2 * np.sin(theta + self.gamma) - self.y2

        N1 = B3 * (
            self.p2 ** 2 - self.p1 ** 2 - A2 ** 2 - B2 ** 2
        ) - B2 * (
            self.p3 ** 2 - self.p1 ** 2 - A3 ** 2 - B3 ** 2
        )
        N2 = -A3 * (
            self.p2 ** 2 - self.p1 ** 2 - A2 ** 2 - B2 ** 2
        ) + A2 * (
            self.p3 ** 2 - self.p1 ** 2 - A3 ** 2 - B3 ** 2
        )
        D = 2 * (A2 * B3 - B2 * A3)

        x = N1 / D
        y = N2 / D

        point_1 = Point(x, y)
        point_2 = Point(
            x + self.L2 * np.cos(theta + self.gamma),
            y + self.L2 * np.sin(theta + self.gamma),
        )
        point_3 = Point(
            x + self.L3 * np.cos(theta),
            y + self.L3 * np.sin(theta),
        )

        return point_1, point_2, point_3

    def draw(self, *thetas, rows=1):
        plt.style.use(
            "https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pacoty.mplstyle"
        )
        fig, axs = plt.subplots(rows, len(thetas) // rows)

        A1, A2, A3 = (
            Point(0, 0),
            Point(self.x2, self.y2),
            Point(self.x1, 0),
        )

        try:
            axs = axs.flatten()
        except:
            pass

        for theta, ax in zip(thetas, axs):
            C1, C2, C3 = self.platform(theta)

            lines = [
                (A1, C1),
                (A2, C2),
                (A3, C3),
                (C1, C2),
                (C2, C3),
                (C3, C1),
            ]
            lines = mc.LineCollection(lines)

            ax.add_collection(lines)
            ax.set_aspect("equal", adjustable="box")

            ax.plot(*A1, "o", label="$(0,0)$")
            ax.plot(*A2, "o", label="$(x_2,y_2)$")
            ax.plot(*A3, "o", label="$(x_1,0)$")
            ax.plot(*C1, "o", label="$(x,y)$")
            ax.plot(
                *C2,
                "o",
                label="$(x + L_2 \\cos{\\theta + \\gamma},y_2 + L_2  \\sin{\\theta + \\gamma})$",
            )
            ax.plot(
                *C3,
                "o",
                label="$(x + L_3 \\cos{\\theta},y_2 + L_3  \\sin{\\theta})$",
            )

            ax.autoscale()

        x_lower = min([a.get_xlim()[0] for a in axs])
        x_upper = max([a.get_xlim()[1] for a in axs])
        y_lower = min([a.get_ylim()[0] for a in axs])
        y_upper = max([a.get_ylim()[1] for a in axs])

        for a in axs:
            a.set_xlim((x_lower, x_upper))
            a.set_ylim((y_lower, y_upper))

        plt.show()

    def plot(self, points=[]):
        plt.style.use(
            "https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pacoty.mplstyle"
        )
        x = np.linspace(-np.pi, np.pi, 1000)
        plt.plot(x, self.f(x))

        for point in points:
            plt.plot(
                point["x"],
                f(point["x"]),
                point["symbol"],
                markersize=12,
                label=point["label"],
            )

        if points:
            plt.legend()

        plt.show()

```


\newpage

## helpers.py

```python

import numpy as np
from itertools import tee
from scipy import optimize

from multiprocessing import Pool
from collections import namedtuple

from f import StewartPlatform


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def find_zero_crossings(
    f, n=1000, lower_bound=-np.pi, upper_bound=np.pi
):
    iterable = (
        (f(x), x)
        for x in np.linspace(
            lower_bound, upper_bound, num=n
        )
    )

    for (a, x1), (b, x2) in pairwise(iterable):
        if np.sign(a) != np.sign(b):
            yield x1, x2


def find_zeros(
    f, n=1000, lower_bound=-np.pi, upper_bound=np.pi
):
    crossings = find_zero_crossings(
        f,
        n=n,
        lower_bound=lower_bound,
        upper_bound=upper_bound,
    )
    return [optimize.bisect(f, a, b) for a, b in crossings]


def draw_system(system):
    zeros = find_zeros(system.f)

    points = [
        {
            "x": zero,
            "symbol": "*",
            "label": f"$x_{i+1} = {system.f(zero):.4e}$",
        }
        for i, zero in enumerate(zeros)
    ]
    system.plot(points)
    system.draw(
        *zeros, rows=int(np.sqrt(len(zeros))) or None
    )


Result = namedtuple("Result", ("x", "n_crossings"))


def find_zero_crossings_for_p2(x):
    test_system = StewartPlatform(
        x1=5,
        x2=0,
        y2=6,
        L1=3,
        L2=3 * np.sqrt(2),
        L3=3,
        gamma=np.pi / 4,
        p1=5,
        p2=x,
        p3=3,
    )
    crossings = list(
        find_zero_crossings(test_system.f, n=500)
    )
    return Result(x, len(crossings))
```

\newpage

Valtýr Örn Kjartansson (vok4) xxx
