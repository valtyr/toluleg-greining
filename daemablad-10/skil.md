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
- '\newcommand{\hwnum}{10}'
- '\newcommand{\hwclass}{STÆ405G}'
- '\newcommand{\hwlecture}{}'
- '\newcommand{\hwsection}{}'
---

\maketitle

# Dæmi {-}

Leysið upphafsgildisverkefnið:

\[
y' = 2\left( t + 1 \right) y, \quad y(0) = 1
\]
á bilinu $[0,1]$ með því að nota aðferð Heun's og reiknið
nálgunargildi $w_i$ fyrir $i = 0,1,2,3,4$ fyrir lausnina
með $h = 0.25$. Þetta er dæmi 1(c) í Excercises 6.2.


\vspace{0.5cm}
**_Svar:_**

Notum aðskilnað breytistærða til að heilda jöfnuna og fáum:

\begin{equation*}
y(t) = C_1e^{(t+1)^2}
\end{equation*}

út frá upphafsskilyrðinu $y(0) = 1$ fáum við að $C_1 = e^{-1}$.

\vspace{0.5cm}

Notum svo Heun forritið frá því í seinustu viku: 

```python

from collections import namedtuple

Result = namedtuple("Result", ("x", "y"))


def heun(dy, x0, y0, h, target):
    x = x0
    y = y0

    yield Result(x=x, y=y)

    while x < target:
        y = y + h / 2 * (
            dy(x, y) + dy(x + h, y + h * dy(x, y))
        )
        x = x + h
        yield Result(x=x, y=y)


if __name__ == "__main__":
    dy = lambda t, y: 2 * (t + 1) * y

    print("\n ====== Heun ====== \n")

    for x, y in heun(dy, 0, 1, 0.25, 1):
        print(f"({x}, {y})")


```

og fáum:

```


$ python3 heun.py


 ====== Heun ====== 

(0, 1)
(0.25, 1.71875)
(0.5, 3.30322265625)
(0.75, 7.070960998535156)
(1.0, 16.793532371520996)

```

þ.e.a.s.:

\begin{equation*}
\begin{aligned}
w_0 &= 1 \\
w_1 &\approx 1.71875 \\
w_2 &\approx 3.30322 \\
w_3 &\approx 1.70710 \\
w_4 &\approx 16.7935
\end{aligned}
\end{equation*}


\newpage


# Dæmi {-}

Breytið eftirfarandi diffurjöfnu í fyrsta stigs diffurjöfnuhneppi:

\[
y'' - 2ty' + 2y = 0
\]

þegar upphafsgildin eru $y(0) = y'(0) = 1$. Notið svo aðferð Heun's
til að reikna $w_i$, $i = 0,1,2,3,4$, með $h = 0.25$. Þetta eru dæmi
3(b) og 4(b) í Excercises 6.3.

\vspace{0.5cm}

**_Svar:_**

Byrjum á að skilgreina tvö ný föll:

\begin{equation*}
\begin{aligned}
x_1(t) &= y(t) \\
x_2(t) &= y'(t)
\end{aligned}
\end{equation*}

athugum að ef við diffrum báðar hliðar jafnanna fá um við:

\begin{equation*}
\begin{aligned}
y_1' &= y' = y_2 \\
y_2' &= y'' = 2ty_2 - 2y_1
\end{aligned}
\end{equation*}

sem má einnig setja fram á fylkjaformi svona:

\begin{equation*}
\begin{bmatrix}
y_1' \\
y_2' 
\end{bmatrix}
=
\begin{bmatrix}
 0 & 1 \\
-2t & 2 
\end{bmatrix}
\begin{bmatrix}
y_1 \\
y_2 
\end{bmatrix}
\end{equation*}

Ég fann ekki neitt um hvernig ætti svo að leysa kerfið með Heun í bókinni :P
var mjög spenntur að gera það samt en jæja. Næst :)

\newpage

# Dæmi {-}

Gerið Dæmi 3 í Exercises 6.4 í bókinni með jöfnunni $y' = 5t^4y$, sjá Dæmi 1(d) í Exercises 6.4.

\vspace{0.5cm}

**_Svar:_**

Skrifum sætt fjórða stigs Runge-Kutta fall með sama snið og Heun forritið að ofan.

```python

from heun import Result


def runge_kutta_4(dy, x0, y0, h, target):
    x = x0
    y = y0

    yield Result(x=x, y=y)

    while x < target:
        s1 = dy(x, y)
        s2 = dy(x + h / 2, y + h / 2 * s1)
        s3 = dy(x + h / 2, y + h / 2 * s2)
        s4 = dy(x + h, y + h * s3)

        y = y + h / 6 * (s1 + 2 * s2 + 2 * s3 + s4)
        x = x + h

        yield Result(x=x, y=y)


if __name__ == "__main__":
    dy = lambda t, y: 5 * t ** 4 * y

    print("\n ====== RK4 ====== \n")

    for x, y in runge_kutta_4(dy, 0, 1, 0.25, 1):
        print(f"({x}, {y})")


```

Úttak forritsins er eftirfarandi:

```

$ python3 rungeKutta.py

 ====== RK4 ====== 

(0, 1)
(0.25, 1.0010175165167918)
(0.5, 1.0318110034012595)
(0.75, 1.2677838925790366)
(1.0, 2.710331356370303)


```

þ.e.a.s.:

\begin{equation*}
\begin{aligned}
w_0 &= 1 \\
w_1 &\approx 1.001 \\
w_2 &\approx 1.0318 \\
w_3 &\approx 1.2678 \\
w_4 &\approx 2.7103
\end{aligned}
\end{equation*}
