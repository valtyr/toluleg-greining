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
- '\newcommand{\hwtype}{Dæmablað}'
- '\newcommand{\hwnum}{5}'
- '\newcommand{\hwclass}{STÆ405G}'
- '\newcommand{\hwlecture}{}'
- '\newcommand{\hwsection}{}'
---

\maketitle

Ég féll frekar mikið á tíma í þessari viku en ég skila því sem ég var kominn með :P

# Dæmi {-}


3. Use Newton's Method to find the two solutions of the system $u^3 - v^3 + u = 0$ and $u^2 + v^2 = 1$.
7. Apply Broyden I with starting guesses $x_0 = (1, 1)$ and $A_0 = I$ to the systems in exercise 3. Report the solutions to as much accuracy as possible and the number of steps required.
8. Apply Broyden II with starting guesses $(1, 1)$ and $B_0 = I$ to the systems in exercise 3. Report the solutions to as much accuracy as possible and the number of steps required.


```{.py include=daemablad-5/newton.py}
```

```


$ python3 daemi1.py

[   array([1, 1]),
    array([ 3., -2.]),
    array([ 1.32608696, -1.26086957]),
    array([ 0.26377473, -1.05035537]),
    array([-1.34843452, -0.89692949]),
    array([-1.50762489,  0.80447168]),
    array([-0.72395978,  0.45818141]),
    array([-0.24628857,  0.41189136]),
    array([0.07222096, 0.32276344]),
    array([0.08701216, 0.14999205]),
    array([0.00818487, 0.09548628])]


```

Ég veit að þetta er ekki að skila réttri niðurstöðu... en það verður bara að hafa það.

\newpage

# Dæmi {-}

Hér er dæmið reiknað í höndunum:

![](daemablad-5/demi2-a.pdf)


Hér er python fall sem skilar Lagrange interpolation fyrir breytilegan fjölda punkta:

```{.py include=daemablad-5/lagrange.py}
```

Og dæmi um niðurstöðu:

```python
import sympy
from langrange import lagrange_interpolation

points = [(-1,0), (2, 1), (3,1), (5,2)]
L = lagrange_interpolation(points)

sympy.plotting.plot(L)
```

```{#transmissionpower .matplotlib format=PDF caption="Samanburður á lagrange margliðu og punktum"}
import sys
import sympy
import matplotlib.pyplot as plt
import numpy as np
sys.path.insert(1, 'daemablad-5/')

from lagrange import lagrange_interpolation

points = [(-1,0), (2, 1), (3,1), (5,2)]
L = lagrange_interpolation(points)

xx = np.linspace(-2.5, 7.5, 1000)
yy = sympy.lambdify(list(L.free_symbols)[0], L)(xx)
plt.plot(xx, np.transpose(yy))
plt.plot([x[0] for x in points], [y[1] for y in points], 'k*')
plt.grid()

```
