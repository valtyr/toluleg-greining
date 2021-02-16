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
- '\newcommand{\hwnum}{2}'
- '\newcommand{\hwclass}{STÆ405G}'
- '\newcommand{\hwlecture}{}'
- '\newcommand{\hwsection}{}'
---

\maketitle

# Dæmi {-}

**Computer problems _1.1.7_**

```{.py include=daemablad-2/daemi1.py}
```

```


$ python3 daemi1.py

SOLUTIONS:
Root x1: -17.18849815108996    Det(x1):  0.000000015005526
Root x2:   9.708299123253994   Det(x2): -0.000000001247258


```

Rót $x_1$ er rétt að 7. aukastaf og rót $x_2$ er rétt að 8.

\newpage

# Dæmi {-}

Which of the following three Fixed-Point Iterations converge to $\sqrt{2}$? Rank the ones that converge from fastest
to slowest.

\begin{align*}
  \text{(A) } x \longrightarrow \frac{1}{2}x + \frac{1}{x} &&
  \text{(B) } x \longrightarrow \frac{2}{3}x + \frac{2}{3x} &&
  \text{(C) } x \longrightarrow \frac{3}{4}x + \frac{1}{2x}
\end{align*}

**_Lausn:_**

```{.py include=daemablad-2/daemi2.py}

```

```

$ python3 daemi2.py

A:  3
B:  10
C:  15


```

Það tók þrjár ítranir fyrir fall A að komast innan vikmarka, 10 fyrir B og 15 fyrir C.
Öll föllin stefna á $\sqrt{2}$ og út frá tölunum að ofan má álykta að A stefni hraðast,
svo B og seinast C.


\newpage


# Dæmi {-}

1. Apply two steps of the Secant Method to the following equation with intial guesses $x_0 = 1$ and $x_1 = 2$.
2. Apply two steps of the Method of False Position with initial bracket [1,2] to the equations of Exercise 1.
3. Apply two steps of Inverse Quadratic Interpolation to the equations of Exercise 1. Use initial guesses $x_0 = 1$, $x_1 = 2$ and $x_2 = 0$, and update by retaining the three most recent.

\[ f(x) = e^x + sin(x) - 4 \]


**_Lausn:_**

```{.py include=daemablad-2/daemi3.py}

```
```

$ python3 daemi3.py

Secant:          1.1193566855644101
False position:  1.1193566855644101
IQI:             1.1292724601823607

```


