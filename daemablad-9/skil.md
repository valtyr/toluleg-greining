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
- '\newcommand{\hwnum}{9}'
- '\newcommand{\hwclass}{STÆ405G}'
- '\newcommand{\hwlecture}{}'
- '\newcommand{\hwsection}{}'
---

\maketitle

# Dæmi {-}

Notið aðskilnað breytistærða til þess að leysa upphafsgildisverkefnið

\[
y' = 2\left( t + 1 \right) y, \quad y(0) = 1
\]

**_Svar:_**

Byrjum á að finna almenna lausn:

\begin{equation*}
\begin{aligned}
y' &= 2(t+1)y \\
\dfrac{y'}{y} &= 2(t+1) \\
\int \dfrac{\dfrac{dy}{dt}}{y}dt &= \int 2(t + 1) dt \\
y &= e^{t(t+2)} + k
\end{aligned}
\end{equation*}

Leysum svo upphafsgildisverkefnið:


\begin{equation*}
\begin{aligned}
1 &= e^{0(0+2)} + k \\
1 &= e^{0} + k \\
k &= 0
\end{aligned}
\end{equation*}

Svo sértæka lausnin er:


\begin{equation*}
y(t) = e^{t(t+2)}
\end{equation*}

Skrifum nú stutt forrit til að reikna euler nálgun:

\vspace{0.5cm}

***

```{.py include=daemablad-9/euler.py}
```

***

\vspace{0.5cm}

Við keyrslu fást nálganirnar:

```


$ python3 euler.py

(0, 1)
(0.25, 1.5)
(0.5, 2.4375)
(0.75, 4.265625)
(1.0, 7.998046875)
(1.25, 15.99609375)
(1.5, 33.99169921875)
(1.75, 76.4813232421875)
(2.0, 181.6431427001953)
(2.25, 454.1078567504883)
(2.5, 1192.0331239700317)
(2.75, 3278.0910909175873)
(3.0, 9424.511886388063)
(3.25, 28273.53565916419)
(3.5, 88354.7989348881)
(3.75, 287153.0965383863)
(4.0, 969141.7008170538)



```

Eða:

| $t$ | $y(t)$ |
|--:|:--|
| 1 | 7.998046875 |
| 2 | 181.6431427001953 |
| 3 | 9424.511886388063 |
| 4 | 969141.7008170538 |

\newpage


# Dæmi {-}

Notið aðskilnað breytistærða til þess að leysa upphafsgildisverkefnið

\[
y' = \dfrac{t^3}{y^2}, \quad y(0) = 1
\]

**_Svar:_**

Byrjum á að finna almenna lausn:

\begin{equation*}
\begin{aligned}
y' &= \dfrac{t^3}{y^2} \\
y'y^2 &= t^3 \\
\int \dfrac{dy}{dt}y^2 dt &= \int t^3 dt \\
y &= \dfrac{\sqrt[\leftroot{-1}\uproot{2}\scriptstyle 3]{3t^4 + 4}}{\sqrt[\leftroot{-1}\uproot{2}\scriptstyle 3]{4}} + k 
\end{aligned}
\end{equation*}

Leysum svo upphafsgildisverkefnið:


\begin{equation*}
\begin{aligned}
1 &= \dfrac{\sqrt[\leftroot{-1}\uproot{2}\scriptstyle 3]{3(0)^4 + 4}}{\sqrt[\leftroot{-1}\uproot{2}\scriptstyle 3]{4}} + k \\
1 &= \dfrac{\sqrt[\leftroot{-1}\uproot{2}\scriptstyle 3]{4}}{\sqrt[\leftroot{-1}\uproot{2}\scriptstyle 3]{4}} + k \\
k &= 0
\end{aligned}
\end{equation*}

Svo sértæka lausnin er:


\begin{equation*}
y = \dfrac{\sqrt[\leftroot{-1}\uproot{2}\scriptstyle 3]{3t^4 + 4}}{\sqrt[\leftroot{-1}\uproot{2}\scriptstyle 3]{4}} 
\end{equation*}

Notum Euler forritið frá því í síðasta dæmi og skrifum Heun nálgunarfall:

\vspace{0.5cm}

***

```{.py include=daemablad-9/heun.py}
```

***


\vspace{0.5cm}

Við keyrslu fást nálganirnar:

```

$ python3 heun.py

 ====== Euler ====== 

(0, 1)
(0.25, 1.0)
(0.5, 1.00390625)
(0.75, 1.034913532472104)
(1.0, 1.133386191966365)
(1.25, 1.3280047157393602)
(1.5, 1.604871472432934)
(1.75, 1.9324634602273811)
(2.0, 2.2912462256644135)
(2.25, 2.6722124471833766)
(2.5, 3.0710036760898682)
(2.75, 3.4851934403155354)
(3.0, 3.913233399780667)
(3.25, 4.354023944097142)
(3.5, 4.806721829171081)
(3.75, 5.270645104938519)
(4.0, 5.745221642279593)

 ====== Heun ====== 

(0, 1)
(0.25, 1.001953125)
(0.5, 1.019342601468375)
(0.75, 1.0822649536177262)
(1.0, 1.2182419316985125)
(1.25, 1.4294310134205817)
(1.5, 1.70047546751946)
(1.75, 2.015154459091792)
(2.0, 2.361960885049574)
(2.25, 2.733595148071747)
(2.5, 3.125464289036878)
(2.75, 3.5345774433017705)
(3.0, 3.95888921606298)
(3.25, 4.3969281408513705)
(3.5, 4.847585271384298)
(3.75, 5.309990630902606)
(4.0, 5.783438464618058)


```

Eða:

| $t$ | $y(t)$ |
|--:|:--|
| 1 | 1.2182419316985125 |
| 2 | 2.361960885049574 |
| 3 | 3.95888921606298 |
| 4 | 5.783438464618058 |
