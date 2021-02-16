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
- '\newcommand{\hwnum}{3}'
- '\newcommand{\hwclass}{STÆ405G}'
- '\newcommand{\hwlecture}{}'
- '\newcommand{\hwsection}{}'
---

\maketitle

# Dæmi {-}

Við höfum $n\times n$ fylki sem er á efra þríhyrningsformi. Það þarf að framkvæma $n^2 = 1.6 \cdot 10^7$ aðgerðir.
Fyrst reikningurinn í heild sinni tekur 2ms að framkvæma hlýtur stök aðgerð að taka
$\frac{0.002}{1.6 \cdot 10^7} = 1,25 \cdot 10^{-10} \text{s} = 125 \text{ps}$.

Nú höfum við venjulegt ferningsfylki sem er $9000 \times 9000$ að stærð. Ef við viljum koma því
á efra þríhyrningsform þurfum við að framkvæma $\frac{2}{3}n^3 + \frac{1}{2}n^2 -\frac{7}{6}n$
aðgerðir og lausnin sjálf krefst svo $9000^2$ aðgerða. Dregið saman eru þetta
$\frac{2}{3}9000^3 + \frac{1}{2}9000^2 -\frac{7}{6}9000 + 9000^2 = 4,86\cdot10^{11}$ aðgerðir í heild.

Notum nú niðurstöðurnar okkar að ofan og fáum tímann sem það tekur að finna lausnina:

 \[
    \left(1,25\cdot10^{-10}\text{ s/aðgerð}\right) \cdot \left(4,86\cdot10^{11}\text{ aðgerðir}\right) \approx 61 \text{ sek}
 \]

\newpage

# Dæmi {-}

**2.2 Computer Problems**

1. Use the code fragments for Gaussian elimination in the previous section to write a Matlab script to take a matrix A as input and output L and U. No row exchanges are allowed—the program should be designed to shut down if it encounters a zero pivot. Check your program by factoring the matrices in Exercise 2.
2. Add two-step back substitution to your script from Computer Problem 1, and use it to solve the systems in Exercise 4.

\vspace{1cm}

**_Lausn:_**

```{.py include=daemablad-3/daemi2_1.py}

```

```

LU factorize:
(array([[1., 0., 0.],
       [2., 1., 0.],
       [1., 0., 1.]]), array([[3, 1, 2],
       [0, 1, 0],
       [0, 0, 3]]))
(array([[1. , 0. , 0. ],
       [1. , 1. , 0. ],
       [0.5, 0.5, 1. ]]), array([[4, 2, 0],
       [0, 2, 2],
       [0, 0, 2]]))
(array([[1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [1., 2., 1., 0.],
       [0., 1., 0., 1.]]), array([[ 1, -1,  1,  2],
       [ 0,  2,  1,  0],
       [ 0,  0,  1,  2],
       [ 0,  0,  0, -1]]))

Solve with back substitution:
[-1.  1.  1.]
[ 1. -1.  3.]


```

Er ekki viss um að lausnirnar séu alveg réttar. Hafði ekki tíma til að athuga þær.

\newpage

