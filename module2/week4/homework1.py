import numpy as np


def compute_mean(X):
    result = 0
    length_num = len(X)
    for num in X:
        result += num
    return result / length_num


X1 = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]
print("Mean:", compute_mean(X1))


def compute_median(X):
    size = len(X)
    X = np.sort(X)
    print("Sorted X:", X)

    if size % 2 == 0:
        median = 1 / 2 * (X[(size // 2) - 1] + X[size // 2])
    else:
        median = X[(size // 2)]
    return median


X2 = [1, 5, 4, 4, 9, 13]
print("Median:", compute_median(X2))


def compute_std(X):
    mean = compute_mean(X)
    variance = 0
    for num in X:
        variance += (num - mean) ** 2
    return np.sqrt(variance / len(X))


X3 = [171, 176, 155, 167, 169, 182]
print("Standard Deviation:", compute_std(X3))


def compute_correlation_cofficient(X, Y):
    X = np.asarray(X, dtype=np.float64)
    Y = np.asarray(Y, dtype=np.float64)
    N = len(X)
    
    total_x = np.sum(X)
    total_y = np.sum(Y)
    total_squared_x = np.sum(X**2)
    total_squared_y = np.sum(Y**2)
    total_x_multiply_y = np.sum(X * Y)
    
    numerator = N * total_x_multiply_y - total_x * total_y
    denominator = np.sqrt(N * total_squared_x - total_x**2) * np.sqrt(N * total_squared_y - total_y**2)
    
    return np.round(numerator / denominator, 2)


X4 = np.asarray([-2, -5, -11, 6, 4, 15, 9])
Y4 = np.asarray([4, 25, 121, 36, 16, 225, 81])
print("Correlation:", compute_correlation_cofficient(X4, Y4))
