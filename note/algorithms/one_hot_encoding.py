import numpy as np

dataset = np.array(
    ["Hanoi", "Tokyo", "London", "Hanoi", "Paris", "Tokyo", "London", "Hanoi"]
)

unique_dataset = set(dataset)

sorted_data = sorted(unique_dataset)

city_index = {city: idx for idx, city in enumerate(sorted_data)}

one_hot_feature = []

for data in dataset:
    one_hot_vector = [0] * len(sorted_data)
    one_hot_vector[city_index[data]] = 1
    one_hot_feature.append(one_hot_vector)

print(sorted_data)
print(one_hot_feature)
