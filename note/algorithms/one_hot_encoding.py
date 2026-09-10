import numpy as np

dataset = np.array([
  'Ho Chi Minh','Da Nang','Ho Chi Minh','Da Nang','Can Tho'
])

set_dataset = set()

for data in dataset:
  set_dataset.add(data)

unique_data = sorted(list(set_dataset))
encoding = {category:id for id,category in enumerate(unique_data)}

one_hot_encoded_feature = []

for data in dataset:
  one_hot_vector = [0] * len(set_dataset)
  one_hot_vector[encoding[data]] = 1
  one_hot_encoded_feature.append(one_hot_vector)

print(one_hot_encoded_feature)