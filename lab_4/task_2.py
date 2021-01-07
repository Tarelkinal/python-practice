from math import fabs, cos, sin, radians, log2, sqrt, log, exp, pow


def func_1(x, y, a, k):
    """x, y in degrees"""
    res = sqrt(fabs(cos(x**2 + radians(44)) + a * sin(k * y)**2)) - 0.6 * y**3 + log2(8)/(4 * a)
    return res


def func_2(x, y):
    res = exp(fabs(4*y - 0.5)) + pow(x, 1/3)/(1 + log(2*x))
    return res
