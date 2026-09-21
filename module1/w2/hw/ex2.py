def count_chars(word:str) -> dict:
    count_dict = {}
    for char in word:
        count_dict[char] = count_dict.get(char, 0) + 1
    return count_dict

# Test case 1
string1 = "Happiness"
print(count_chars(string1))
# Output mong đợi: {'H': 1, 'a': 1, 'p': 2, 'i': 1, 'n': 1, 'e': 1, 's': 2}

# Test case 2
string2 = "smiles"
print(count_chars(string2))
# Output mong đợi: {'s': 2, 'm': 1, 'i': 1, 'l': 1, 'e': 1}
