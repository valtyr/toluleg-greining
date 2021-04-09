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
- '\newcommand{\hwnum}{6}'
- '\newcommand{\hwclass}{STÆ405G}'
- '\newcommand{\hwlecture}{}'
- '\newcommand{\hwsection}{}'
---

\maketitle

# Dæmi {-}

Find the equations and plot the natural cubic spline that interpolates the data points 

a) $(0,3), (1,5), (2,4), (3,1)$
b) $(-1,3), (0,5), (3,1), (4,1), (5,1)$.

\answerheader{Svar:}

Eftirfarandi er forrit sem notað var við útreikningana:

```{.py include=daemablad-6/splines.py}
```

\newpage

Hér eru stuðlarnir fyrir a:

\begin{equation*}
C_a = \begin{bmatrix}
2.6666666666666665 & 0.0 & -0.6666666666666666 \\
0.6666666666666667 & -2.0 & 0.3333333333333333 \\
-2.3333333333333335 & -1.0 & 0.3333333333333333
\end{bmatrix}
\end{equation*}

og hér er mynd:

```{#transmissionpower .matplotlib format=PDF caption="Fjaðurbrúunarferill í gegn um punkta a"}

import sys
sys.path.insert(1, 'daemablad-6/')

from splines import a, cubic_spline_plot
cubic_spline_plot(a, 1000)

```

\newpage

Hér eru stuðlarnir fyrir b:

\begin{equation*}
C_b = \begin{bmatrix}
2.5628930817610063 & 0.0 & -0.5628930817610063 \\
0.8742138364779872 & -1.6886792452830188 & 0.31761006289308175 \\
-0.6823899371069183 & 1.169811320754717 & -0.48742138364779874 \\
0.19496855345911948 & -0.29245283018867924 & 0.09748427672955974
\end{bmatrix}
\end{equation*}

og hér er mynd:

```{#transmissionpower .matplotlib format=PDF caption="Fjaðurbrúunarferill í gegn um punkta b"}

import sys
sys.path.insert(1, 'daemablad-6/')

from splines import b, cubic_spline_plot
cubic_spline_plot(b, 1000)
```

\newpage

# Dæmi {-}

Fit data to the periodic model $y = F_3(t) = c_1 + c_2 cos(2\pi t) + c_3 sin(2\pi t)$. Find the 2-norm error and the RMSE.

\vspace{0.5cm}

|    t     |   y   |
|:-----:|:-:|
| 0     |1|
| $1/4$ |3|
| $1/2$ |2|
| $3/4$ |0|

\answerheader{Svar:}

Eftirfarandi forrit var notað til útreikninga:

```{.py include=daemablad-6/fit.py}
```

\newpage

Keyrum kóðann í IPython:

```


$ ipython -i fit.py

In [1]: x, err = fit(data)

In [2]: calculate_error(data, err)
Out[2]:
[-0.06240098941341854,
 -0.06799355793418127,
 0.7733474685692601,
 -1.0189282944650282]

In [3]: plot(data, x)


```

Út kemur eftirfarandi mynd:

```{#transmissionpower .matplotlib format=PDF caption="Mynd af sniðnu falli"}

import sys
sys.path.insert(1, 'daemablad-6/')

from fit import data, fit, plot

x, err = fit(data)
plot(data, x)
```

\newpage

# Dæmi {-}

Apply classical Gram–Schmidt orthogonalization to find the full QR factorization of the following matrix:

\begin{equation*}
\begin{bmatrix}
4 & 8 & 1 \\
0 & 2 & -2 \\
3 & 6 & 7
\end{bmatrix}
\end{equation*}

\answerheader{Svar:}

Skrifaði eftirfarandi kóðabút út frá pseudokóðanum í bókinni. Hann virkar ekki... en ég fann ekki villuna og ég er að drífa mig :)
\vspace{0.5cm}

```{.py include=daemablad-6/qr.py}
```

\vspace{0.5cm}

Úttakið er: 

\begin{equation*}
A = \begin{bmatrix}
0.8 & 0.784465 & 0.136083 \\
0.0 & 0.196116 & -0.272166 \\
0.6 & 0.588348 & 0.952579
\end{bmatrix}
\begin{bmatrix}
5.0 & 0.0 & 0.0 \\
0.0 & 10.19804 & 0.0 \\
7.34847 & 0.0 & 7.34847
\end{bmatrix}
\end{equation*}

sem er kolvitlaust :P
