import numpy as np


def create_train_data():
    data = [
        ["Sunny", "Hot", "High", "Weak", "no"],
        ["Sunny", "Hot", "High", "Strong", "no"],
        ["Overcast", "Hot", "High", "Weak", "yes"],
        ["Rain", "Mild", "High", "Weak", "yes"],
        ["Rain", "Cool", "Normal", "Weak", "yes"],
        ["Rain", "Cool", "Normal", "Strong", "no"],
        ["Overcast", "Cool", "Normal", "Strong", "yes"],
        ["Overcast", "Mild", "High", "Weak", "no"],
        ["Sunny", "Cool", "Normal", "Weak", "yes"],
        ["Rain", "Mild", "Normal", "Weak", "yes"],
    ]
    return np.array(data)


def compute_prior_probablity(train_data):
    y_unique = ["no", "yes"]
    prior_probability = np.zeros(len(y_unique))
    prior_probability[0] = np.mean(train_data[:, 4] == y_unique[0])
    prior_probability[1] = np.mean(train_data[:, 4] == y_unique[1])
    return prior_probability


def compute_conditional_probability(train_data:np.ndarray):
    y_unique = ["no", "yes"]
    conditional_probability = []
    list_x_name = []
    for i in range(train_data.shape[1] - 1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)
        x_conditional_probability = np.zeros([len(y_unique), len(x_unique)])
        for j in range(len(y_unique)):
            label = np.sum(train_data[:, -1] == y_unique[j])
            for k in range(len(x_unique)):
                value_feature = np.sum(
                    (train_data[:, -1] == y_unique[j])
                    & (train_data[:, i] == x_unique[k])
                )
                x_conditional_probability[j, k] = value_feature / label
        conditional_probability.append(x_conditional_probability)
    return conditional_probability, list_x_name

def get_index_from_value(feature_name, list_features):
    return np.where(list_features == feature_name)[0][0]


def train_naive_bayes(train_data):
    # Step 1: Calculate Prior Probability
    prior_probability = compute_prior_probablity(train_data)

    # Step 2: Calculate Conditional Probability
    conditional_probability, list_x_name = compute_conditional_probability(train_data)

    return prior_probability, conditional_probability, list_x_name


def prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability):
    x1 = get_index_from_value(X[0], list_x_name[0])
    x2 = get_index_from_value(X[1], list_x_name[1])
    x3 = get_index_from_value(X[2], list_x_name[2])
    x4 = get_index_from_value(X[3], list_x_name[3])
    
    p0 = prior_probability[0] * conditional_probability[0][0,x1] * conditional_probability[1][0,x2]  * conditional_probability[2][0,x3] * conditional_probability[3][0,x4] 
    p1 = prior_probability[1]  * conditional_probability[0][1,x1] * conditional_probability[1][1,x2]  * conditional_probability[2][1,x3] * conditional_probability[3][1,x4] 
    
    if p0 > p1:
        y_pred = 0
    else:
        y_pred = 1

    return y_pred


train_data = create_train_data()
prior_probability = compute_prior_probablity(train_data)
print("P(play tennis = No):", prior_probability[0])
print("P(play tennis = Yes):", prior_probability[1])

_, list_x_name = compute_conditional_probability(train_data)
print("x1 = ", list_x_name[0])
print("x2 = ", list_x_name[1])
print("x3 = ", list_x_name[2])
print("x4 = ", list_x_name[3])

_, list_x_name = compute_conditional_probability(train_data)
outlook = list_x_name[0]

i1 = get_index_from_value("Overcast", outlook)
i2 = get_index_from_value("Rain", outlook)
i3 = get_index_from_value("Sunny", outlook)
print(i1, i2, i3)

conditional_probability, list_x_name = compute_conditional_probability(train_data)

# Compute P("Outlook"="Sunny" | "Play Tennis"="Yes")
x1 = get_index_from_value("Sunny", list_x_name[0])
print(
    "P(Outlook='Sunny'|Play Tennis='Yes')",
    np.round(conditional_probability[0][1, x1], 2),
)
X = ["Sunny", "Cool", "High", "Strong"]
data = create_train_data()
prior_probability, conditional_probability, list_x_name = train_naive_bayes(data)
pred = prediction_play_tennis(
    X, list_x_name, prior_probability, conditional_probability
)

if pred:
    print("Ad should go!")
else:
    print("Ad should not go!")
