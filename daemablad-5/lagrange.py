import sympy
from functools import reduce


def lagrange_interpolation(points):
    x = sympy.symbols("x")

    terms = []
    for k, point in enumerate(points):
        numerator_parts = [
            x - points[i][0]
            for i in range(len(points))
            if i != k
        ]
        denominator_parts = [
            point[0] - points[i][0]
            for i in range(len(points))
            if i != k
        ]

        frac = reduce(
            lambda a, b: a * b, numerator_parts
        ) / reduce(lambda a, b: a * b, denominator_parts)
        terms.append(point[1] * frac)

    expression = reduce(lambda a, b: a + b, terms)
    return sympy.simplify(expression)
