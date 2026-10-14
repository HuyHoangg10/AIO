import string
import nltk

nltk.download("stopwords", quiet=True)
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder


# read csv
DATASET_PATH = "./data/2cls_spam_text_cls.csv"
df = pd.read_csv(DATASET_PATH)

messages = df["Message"].values.tolist()
labels = df["Category"].values.tolist()


# data preprocessing
def lowercase(text):
    return text.lower()


def punctuation_removal(text):
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator)


def tokenize(text):
    return nltk.word_tokenize(text)


def remove_stopwords(tokens):
    stop_word = nltk.corpus.stopwords.words("english")
    return [token for token in tokens if token not in stop_word]


def stemming(tokens):
    stemmer = nltk.PorterStemmer()
    return [stemmer.stem(token) for token in tokens]


def preprocess_text(text):
    text = lowercase(text)
    text = punctuation_removal(text)
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens)
    tokens = stemming(tokens)

    return tokens


messages = [preprocess_text(message) for message in messages]

# create dictionary
def create_dictionary(messages):
    dictionary = []
    for tokens in messages:
        for token in tokens:
            if token not in dictionary:
                dictionary.append(token)
    return dictionary

# create feature
def create_features(tokens,dictionary):
    feature = np.zeros(len(dictionary))

    for token in tokens:
        if token in dictionary:
            feature[dictionary.index(token)] += 1
    return feature

#encode labels
le = LabelEncoder()
y = le.fit_transform(labels)

dictionary = create_dictionary(messages)
X = np.array([create_features(tokens, dictionary) for tokens in messages])

#split dataset : train , val , test
VAL_SIZE = 0.2
TEST_SIZE = 0.125
SEED = 0
IS_SHUFFLE = True

X_train, X_val, y_train, y_val = train_test_split(
    X, y,
    test_size=VAL_SIZE,
    shuffle=IS_SHUFFLE,
    random_state=SEED
)

X_train, X_test, y_train, y_test = train_test_split(
    X_train, y_train,
    test_size=TEST_SIZE,
    shuffle=IS_SHUFFLE,
    random_state=SEED
)

model = GaussianNB()
model.fit(X_train,y_train)

y_val_pred = model.predict(X_val)
y_test_pred = model.predict(X_test)
val_accuracy = accuracy_score(y_val, y_val_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)
# print(f'Val accuracy: {val_accuracy}')
# print(f'Test accuracy: {test_accuracy}')

def predict(text,model,dictionary):
    processed_text = preprocess_text(text)
    feature = create_features(processed_text,dictionary)
    feature = np.array(feature).reshape(1,-1)
    prediction = model.predict(feature)
    prediction_cls = le.inverse_transform(prediction)[0]
    return prediction_cls

input = "I am a champion"
prediction = predict(input,model,dictionary)
print(prediction)
