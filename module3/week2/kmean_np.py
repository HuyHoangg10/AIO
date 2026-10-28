import numpy as np
import pandas as pd

# Load dataset
df = pd.read_csv("iris.csv")
cols = ["sepal_length", "sepal_width"]
X = df[cols].to_numpy()


class KMeans:
    def __init__(self, k=3, max_iters=100):
        self.k = k
        self.max_iters = max_iters
        self.centroids = None
        self.clusters = None

    def euclid_distance(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2))

    def initialize_centroids(self, data):
        np.random.seed(42)
        self.centroids = data[np.random.choice(data.shape[0], self.k, replace=False)]

    def assign_clusters(self, data):
        distances = np.array(
            [
                [self.euclid_distance(x, centroid) for centroid in self.centroids]
                for x in data
            ]
        )
        return np.argmin(distances, axis=1)

    def update_centroids(self, data):
        return np.array([data[self.clusters == i].mean(axis=0) for i in range(self.k)])

    def fit(self, data):
        self.initialize_centroids(data)
        for i in range(self.max_iters):
            self.clusters = self.assign_clusters(data)
            new_centroids = self.update_centroids(data)
            if np.all(self.centroids == new_centroids):
                break
            self.centroids = new_centroids


model = KMeans(k=3, max_iters=100)
model.fit(X)

print(model.centroids)
print(model.clusters[:10])