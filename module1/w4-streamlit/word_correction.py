import streamlit as st

def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words

def levenshtein_distance(source: str, target: str) -> int:
    dp = [[0] * (len(target) + 1) for _ in range(len(source) + 1)]

    for i in range(len(source) + 1):
        dp[i][0] = i

    for j in range(len(target) + 1):
        dp[0][j] = j

    for i in range(1, len(source) + 1):
        for j in range(1, len(target) + 1):
            cost = 0 if source[i - 1] == target[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + cost
            )
    return dp[-1][-1]

vocabs = load_vocab(file_path='./vocab.txt')

st.title('Word Correction')
word = st.text_input("Your Word")

if st.button("Compute"):
    distances = {}
    for vocab in vocabs:
        distance = levenshtein_distance(word, vocab)
        distances[vocab] = distance
    sorted_distances = dict(sorted(distances.items(), key=lambda item: item[1]))
    correct_word = list(sorted_distances.keys())[0]
    st.write('Correct: ', correct_word)

    col1, col2 = st.columns(2)
    col1.write(vocabs)

    col2.write(sorted_distances)