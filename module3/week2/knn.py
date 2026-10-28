from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

# read data
df = pd.read_csv("iris.csv")
columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
X = df[columns].to_numpy()
y = df["species"].to_numpy()

# split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# scale data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# model and train
knn_classifier = KNeighborsClassifier()
knn_classifier.fit(X_train, y_train)

# predict
y_pred = knn_classifier.predict(X_test)
print(f"Score: {accuracy_score(y_test, y_pred)}")
