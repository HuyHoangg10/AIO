import math


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


def exercice2(x, activation_function):
    if not is_number(x):
        print("x must be a number")
        return
    if activation_function not in ("sigmoid", "elu", "relu"):
        print(f"{activation_function} is not supported")
        return
    x = float(x)
    if activation_function == "sigmoid":
        sigmoid = 1 / (1 + math.exp(-x))
        print(f"sigmoid = {sigmoid}")
    if activation_function == "relu":
        if x <= 0:
            relu = 0
        else:
            relu = x
        print(f"relu = {relu}")
    if activation_function == "elu":
        if x <= 0:
            elu = 0.01 * (math.e**x - 1)
        else:
            elu = x
        print(f"elu = {elu}")

exercice2("abc", "sigmoid")