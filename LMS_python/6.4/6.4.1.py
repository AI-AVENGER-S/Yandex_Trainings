from math import sin, cos, pi, tan
from sys import stdin


def ctg(x):
    return cos(x) / sin(x)


def f(x):
    return (cos(x + pi) * cos(3 * pi / 2 - x) * tan(x + 3 * pi / 2)) / (
        sin(pi / 2 - x) * sin(3 * pi / 2 - x) * ctg(x + pi)
    )


for x in stdin:
    print("%.3f" % (f(float(x))))
