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

\answerheader{Solution:}

\newpage

# Problem {-}

Write a program that, for any input s between 0 and 1, finds the parameter $t^\ast(s)$ that is s of the way along the curve. In other words, the arc length from $t = 0$ to $t = t^\ast(s)$ divided by the arc length from $t = 0$ to $t = 1$ should be equal to s.
Use the Bisection Method to locate the point $t^\ast(s)$ to three correct decimal places. What function is being set to zero? What bracketing interval should be used to start the Bisection Method?

\answerheader{Solution:}

\newpage

# Problem {-}

Equipartition the path of Figure 5.6 into n subpaths of equal length, for $n = 4$ and $n = 20$. Plot analogues of Figure 5.6, showing the equipartitions. If your computations are too slow, consider speeding up the Adaptive Quadrature with Simpson’s Rule, as suggested in Computer Problem 5.4.2.

\answerheader{Solution:}

\newpage

# Problem {-}

Replace the Bisection Method in Step 2 with Newton’s Method, and repeat Steps 2 and 3. What is the derivative needed? What is a good choice for the initial guess? Is computation time decreased by this replacement?

\answerheader{Solution:}

\newpage

# Problem {-}

Use Matlab’s animation commands to demonstrate traveling along the path, first at the original parameter $0 \leq t \leq 1$ speed and then at the (constant) speed given by $t^\ast (s)$ for $0 \leq s \leq 1$.

\answerheader{Solution:}

https://youtu.be/zXql5pZieag

\newpage

# Problem {-}

Experiment with equipartitioning a path of your choice. Build a design, initial, etc. of your choice out of Bézier curves, partition it into equal arc length segments, and animate as in Step 5.

\answerheader{Solution:}

https://youtu.be/rIlYoyvWUgg

\newpage

# Problem{-}

Write a program that traverses the path P according to an arbitrary progress curve $C(s)$, $0 \leq s \leq 1$, with $C(0) = 0$ and $C(1) = 1$. The object is to move along the curve C in such a way that the proportion $C(s)$ of the path’s total arc length is traversed between 0 and s. For example, constant speed along the path would be represented by $C(s) = s$. Try progress curves:

- $C(s) = s^{\frac{1}{3}}$
- $C(s) = s^2$
- $C(s) = sin(s \frac{\pi}{2})$
- $C(s) = \frac{1}{2} + \frac{1}{2}sin(2s - 1)\frac{\pi}{2}$

, for example.

\answerheader{Solution:}

https://youtu.be/YL2z40-pVb8

\newpage
