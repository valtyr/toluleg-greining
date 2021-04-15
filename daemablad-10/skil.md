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
x_1' &= y' = x_2 \\
x_2' &= y'' = 2ty' - 2y = 2tx_2 - 2x_1
\end{aligned}
\end{equation*}

