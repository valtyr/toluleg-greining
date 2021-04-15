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

Write a function that uses Adaptive Quadrature to compute the arc length from $t = 0$ to $t = T$
for a given $T \leq 1$.

\answerheader{Svar:}

```python

def adaptive_quad_length_T(T, f, tolerance=0.005):
    def s(a, b):
        return (b - a) * ((f(a) + f(b)) / 2)

    def quad(a, b, a_orig, b_orig):
        c = (a + b) / 2

        s_ab = s(a, b)
        s_ac = s(a, c)
        s_cb = s(c, b)

        criterion = (
            s_ab - s_ac - s_cb
            < 3 * tolerance * ((b - a) / (b_orig - a_orig))
        )

        if criterion:
            return s_ac + s_cb
        else:
            return quad(a, c, a_orig, b_orig) + quad(
                c, b, a_orig, b_orig
            )

    return quad(0, T, 0, T)

if __name__ == "__main__":
    from Definitions import f

    length = adaptive_quad_length_T(1, f)
    print(length)


```

(Fallið f er skilgreint í [`Definitions.py`](https://github.com/valtyr/toluleg-greining/blob/master/verkefni2/Definitions.py)).

```
$ python3 AdaptiveQuadrature.py

2.4576782863193145

```

\newpage

# Problem {-}

Write a program that, for any input s between 0 and 1, finds the parameter $t^\ast(s)$ that is s of the way along the curve. In other words, the arc length from $t = 0$ to $t = t^\ast(s)$ divided by the arc length from $t = 0$ to $t = 1$ should be equal to s.
Use the Bisection Method to locate the point $t^\ast(s)$ to three correct decimal places. What function is being set to zero? What bracketing interval should be used to start the Bisection Method?

\answerheader{Svar:}

```python

import numpy as np
from scipy.optimize import bisect

def optimization_function(t, s, f):
    return s - adaptive_quad_length_T(
        t, f
    ) / adaptive_quad_length_T(1, f)


def find_t_for_s(s, f):
    return bisect(
        lambda t: optimization_function(
            t, s, f
        ),
        -1 + 0.01,
        1.1,
    )

if __name__ == "__main__":
    from Definitions import f

    # Find t so that length from 0 to t = 0.5
    t_bisect = find_t_for_s(1 / 2, f)
    print("T: ", t_bisect)

```

Fallið sem leitað er að rótum í er mismunurinn á s og hlutafallinu
milli lengd að t og heildarlengd ferilsins. Hér notum við endapunkta stikans (0, 1)
sem upphafspunkta í bisect, en þeir eru líklega ekki besti kosturinn. Þó er tryggt að þeir
séu sitthvoru megin við 0.

Niðurstaðan fyrir $s=\frac{1}{2}$ er:

```

$ python3 TStarS.py

0.8036166227625561

```

\newpage

# Problem {-}

Equipartition the path of Figure 5.6 into n subpaths of equal length, for $n = 4$ and $n = 20$. Plot analogues of Figure 5.6, showing the equipartitions. If your computations are too slow, consider speeding up the Adaptive Quadrature with Simpson’s Rule, as suggested in Computer Problem 5.4.2.

\answerheader{Svar:}

```python

from TStarS import find_t_for_s


def equipartition(f, n):
    length = 1 / n
    return [
        find_t_for_s(length * i, f, simpson=True)
        for i in range(1, n + 1)
    ]


```

Fallið er tiltölulega einfalt. Það kallar í `find_t_for_s` með $i \frac{1}{n}$
þar sem fyrir allar heiltölur $i$ frá $1$ og upp í $n$.

Aðferð Simpson var útfærð í `find_t_for_s`.

```{.matplotlib format=PDF caption="P brotið upp í 4 búta af jafnri lengd"}

import sys
sys.path.insert(1, './verkefni2')

from Equipartition import draw_partitions, equipartition
from Definitions import f

partitions_4 = equipartition(f, 4)

draw_partitions(partitions_4)

```

```{.matplotlib format=PDF caption="P brotið upp í 20 búta af jafnri lengd"}

import sys
sys.path.insert(1, './verkefni2')

from Equipartition import draw_partitions, equipartition
from Definitions import f

partitions_20 = equipartition(f, 20)

draw_partitions(partitions_20)

```

\newpage

# Problem {-}

Replace the Bisection Method in Step 2 with Newton’s Method, and repeat Steps 2 and 3. What is the derivative needed? What is a good choice for the initial guess? Is computation time decreased by this replacement?

\answerheader{Svar:}

Skiptum yfir í newton, notum three-point centered-difference sem nálgun á afleiðu og 0.6 sem gisk.
Keyrum svo bæði föllin 1000 sinnum venjulega og 100 sinnum með Simpson. Prentum út meðaltíma hverrar
keyrslu. Þau skila öll um það bil sömu niðurstöðum fyrir dæmi 2, og eins fyrir dæmi 3.

```python

import numpy as np
from scipy.optimize import newton

def find_t_for_s_newton(s, f, h=0.0001, simpson=True):
    # Three-point centered-difference (5.7)
    def optimization_prime(t):
        return (
            optimization_function(
                t + h, s, f, simpson=simpson
            )
            - optimization_function(
                t - h, s, f, simpson=simpson
            )
        ) / (2 * h)

    # Tried using s as initial guess but got strange errors
    # Using 0.6 as initial guess
    return newton(
        lambda t: optimization_function(
            t, s, f, simpson=simpson
        ),
        0.6,
        fprime=optimization_prime,
    )


if __name__ == "__main__":
    import time
    import random
    from Definitions import f

    def get_avg_time(repeats, function):
        start_time = time.perf_counter()
        for _ in range(repeats):
            function()
        return (time.perf_counter() - start_time) / repeats

    # Find t so that length from 0 to t = 0.5
    t_bisect = find_t_for_s(1 / 2, f, simpson=False)
    t_bisect_simpson = find_t_for_s(1 / 2, f)
    t_newton = find_t_for_s(1 / 2, f, simpson=False)
    t_newton_simpson = find_t_for_s(1 / 2, f)
    print("Bisect:          ", t_bisect)
    print("Bisect simpson:  ", t_bisect_simpson)
    print("Newton:          ", t_newton)
    print("Newton simpson:  ", t_newton_simpson)

    bisect_time = get_avg_time(
        1000,
        lambda: find_t_for_s(
            random.random(), f, simpson=False
        ),
    )
    bisect_simpson_time = get_avg_time(
        1000, lambda: find_t_for_s(random.random(), f)
    )
    newton_time = get_avg_time(
        1000,
        lambda: find_t_for_s_newton(
            random.random(), f, simpson=False
        ),
    )
    newton_simpson_time = get_avg_time(
        1000,
        lambda: find_t_for_s_newton(random.random(), f),
    )

    print("Bisect time:          ", bisect_time)
    print("Bisect simpson time:  ", bisect_simpson_time)
    print("Newton time:          ", newton_time)
    print("Newton simpson time:  ", newton_simpson_time)


```

Newton með Simpson er miklu hraðara en bisect, en bisect með Simpson kemst mjög nálægt.

```


$ python3 TStarS.py

Bisect:           0.8036166227625561
Bisect simpson:   0.7994447956758721
Newton:           0.8036166227625561
Newton simpson:   0.7994447956758721

Bisect time:           0.010633493592999999
Bisect simpson time:   0.005611066451000001
Newton time:           0.005487388963000001
Newton simpson time:   0.004230671486999999

```

\newpage

# Problem {-}

Use animation commands to demonstrate traveling along the path, first at the original parameter $0 \leq t \leq 1$ speed and then at the (constant) speed given by $t^\ast (s)$ for $0 \leq s \leq 1$.

\answerheader{Svar:}

Ég notaði hið frábæra kóðasafn Manim frá 3Blue1Brown til þess að búa til hreyfimyndirnar.
Kóðann á bak við dæmið má finna í Balls klasa [`Animation.py`](https://github.com/valtyr/toluleg-greining/blob/8f1a67f95a8336982f743bd172b7d31dffc97152/verkefni2/Animation.py#L63) skjalsins.

Hér má finna hreyfimyndina: [https://youtu.be/zXql5pZieag](https://youtu.be/zXql5pZieag).

\newpage

# Problem {-}

Experiment with equipartitioning a path of your choice. Build a design, initial, etc. of your choice out of Bézier curves, partition it into equal arc length segments, and animate as in Step 5.

\answerheader{Svar:}

Ég valdi Bezier ferilinn sem er skilgreindur út frá punktunum
$(0, 0)$, $(2, 2)$, $(-1, 2)$, og $(1, 0)$. Kóðann fá finna í klasanum MyBalls í [`ValtyrAnimation.py`](https://github.com/valtyr/toluleg-greining/blob/8f1a67f95a8336982f743bd172b7d31dffc97152/verkefni2/ValtyrAnimation.py#L55).

Hér má finna hreyfimyndina: [https://youtu.be/rIlYoyvWUgg](https://youtu.be/rIlYoyvWUgg).

\newpage

# Problem{-}

Write a program that traverses the path P according to an arbitrary progress curve $C(s)$, $0 \leq s \leq 1$, with $C(0) = 0$ and $C(1) = 1$. The object is to move along the curve C in such a way that the proportion $C(s)$ of the path’s total arc length is traversed between 0 and s. For example, constant speed along the path would be represented by $C(s) = s$. Try progress curves:

- $C(s) = s^{\frac{1}{3}}$
- $C(s) = s^2$
- $C(s) = sin(s \frac{\pi}{2})$
- $C(s) = \frac{1}{2} + \frac{1}{2}sin(2s - 1)\frac{\pi}{2}$

, for example.

\answerheader{Svar:}

Það er mjög einfalt að útfæra þessa virkni. Ef s er hlutfall hreyfimyndar sem búið er að spila
þá er t = C(s). Breytan t er svo notuð sem inntak í stikaföllin. Þetta er oft kallað "timing function"
eða "rate function". Raunar er þessi virkni þegar til í Manim safninu svo ég þurfti bara að útfæra
föllin sjálf.

```python

class TimingFunctions:
    @staticmethod
    def linear(t):
        return t

    @staticmethod
    def third_root(t):
        return t ** (1 / 3)

    @staticmethod
    def t_squared(t):
        return t ** 2

    @staticmethod
    def sin(t):
        return np.sin(t * (np.pi / 2))

    @staticmethod
    def equation(t):
        return 1 / 2 + (1 / 2) * np.sin(2 * t - 1) * (
            np.pi / 2
        )

```

Allan kóða hreyfimyndarinnar má finna í klasanum `TimingFunctionsScene` í [`Animation.py`](https://github.com/valtyr/toluleg-greining/blob/8f1a67f95a8336982f743bd172b7d31dffc97152/verkefni2/Animation.py#L132) skjalinu.

Í eftirfarandi myndbandi má sjá niðurstöðuna fyrir hvert fall: [https://youtu.be/YL2z40-pVb8](https://youtu.be/YL2z40-pVb8)

\newpage

---

## Annað

Valtýr Örn Kjartansson xxx

Allan kóða sem tilheyrir þessu verkefni má finna á slóðinni: [https://github.com/valtyr/toluleg-greining/tree/master/verkefni2](https://github.com/valtyr/toluleg-greining/tree/master/verkefni2)
