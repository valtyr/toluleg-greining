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
- '\newcommand{\hwnum}{1}'
- '\newcommand{\hwclass}{STÆ405G}'
- '\newcommand{\hwlecture}{}'
- '\newcommand{\hwsection}{}'
---

\maketitle

# Dæmi {-}

**Computer problems _0.1.1_**

```python

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


```

```
$ python3 daemi1.py
4.760636329592671e-12


```


**Computer problems _0.1.2_**

```python

import numpy as np
from daemi1 import nest

x = 1.00001
a = nest(99, np.ones(100), -x, np.zeros(99))
b = (np.power(-x, 100) - 1) / (-x - 1)
print(a - b)


```

```
$ python3 daemi2.py
-1.713039432527097e-16
```

# Dæmi {-}

Explain how to most accurately compute the two roots of the equation $x^2 + bx - 10^{-12} = 0$, where b is a number greater than 100.

**_Lausn:_**

Á blaðsíðu 18 í bókinni er talað um nákvæmlega þetta vandamál. Þegar $4\abs{ac} \ll b^2$ eru $b$ og $\sqrt{b^2 - 4ac}$
af nánast sömu stærðargráðu lendum við í vandræðum með nákvæmni í útreikningi annarrar rótarinnar.

Fyrst $b$ er jákvæð stærð í okkar tilfelli getum við notað jöfnurnar:

\begin{align*}
  x_1 = - \frac{ b + \sqrt{ b^2 - 4ac } }{2a} && \text{og} &&  x_2 = - \frac{2c}{(b + \sqrt{b^2 - 4ac} )}
\end{align*}

þar sem $a = 1$ og $c = 10^{-12}$.



# Dæmi {-}

Reiknið fl(8.7) og ritið niðurstöðuna á hex-formati. Sýnið að um hlutfallsskekkjuna gildi

\[ \frac{ \abs{ \text{fl}(-8.7) - (-8.7)  } }{ \abs{ -8.7 } } \geq \frac{\epsilon_{mach}}{2} \]

**_Lausn:_**




