import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data = pd.read_csv("advertising.csv")
print(data)


#5
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
    denominator = np.sqrt(N * total_squared_x - total_x**2) * np.sqrt(
        N * total_squared_y - total_y**2
    )

    return np.round(numerator / denominator, 2)


def correlation(x, y):
    return compute_correlation_cofficient(x, y)


x = data["TV"]
y = data["Radio"]
corr_xy = correlation(x, y)
print(f"Câu 5 - Correlation giữa TV và Radio: {round(corr_xy, 2)}")

#6
features = ["TV", "Radio", "Newspaper"]

for i in range(len(features)):
    for j in range(len(features)):
        corr_value = correlation(data[features[i]], data[features[j]])
        print(
            f"Correlation between {features[i]} and {features[j]}: {round(corr_value, 2)}"
        )

#7
x = data["Radio"]
y = data["Newspaper"]

result = np.corrcoef(x, y)
print(result)

#8
data_corr = data.corr()
print(data_corr)

#9 
plt.figure(figsize=(10, 8))
sns.heatmap(data_corr,annot=True,fmt=".2f",linewidths=.5)
plt.show()