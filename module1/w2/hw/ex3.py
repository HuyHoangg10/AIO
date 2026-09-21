def count_word(file_path: str) -> dict:
    with open(file_path, "r") as file:
        words = file.read().lower().split()

    count_dict = {}
    for word in words:
        count_dict[word] = count_dict.get(word, 0) + 1

    return count_dict