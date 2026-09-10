import math


def cal_factorial(number):
    if not isinstance(number, int):
        return "Number must be integer"
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


def approx_sin(x, n):
    total = 0
    for i in range(n + 1):
        sin = ((-1) ** i) * ((math.pow(x, 2 * i + 1)) / cal_factorial(2 * i + 1))
        total += sin
    return total


def approx_cos(x, n):
    total = 0
    for i in range(n + 1):
        cos = ((-1) ** i) * ((math.pow(x, 2 * i)) / cal_factorial(2 * i))
        total += cos
    return total


def approx_cosh(x, n):
    total = 0
    for i in range(n + 1):
        cosh = (math.pow(x, 2 * i)) / cal_factorial(2 * i)
        total += cosh
    return total


def approx_sinh(x, n):
    total = 0
    for i in range(n + 1):
        sinh = (math.pow(x, 2 * i + 1)) / cal_factorial(2 * i + 1)
        total += sinh
    return total
