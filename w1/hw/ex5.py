import math


def exercise5(y, y_hat, n, p):
    root_n_of_y = y ** (1 / n)
    root_n_of_y_hat = y_hat ** (1 / n)
    loss = math.pow(root_n_of_y - root_n_of_y_hat, p)
    return loss

print(exercise5(99.5, 100, 2, 0.5))