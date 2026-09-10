# ==============================================================================
# 1. INITIALIZATION & READ 
# ==============================================================================
player = ["Bruno", "Harry", "Cunha"]
sub_player = ["Tyler", "Amad", "Bryan"]

print(f"Original player list: {player}")


# ==============================================================================
# 2. CREATE / INSERT 
# ==============================================================================
# .append()  -> Add an element to the END of the list
player.append("Senne")

# .insert()  -> Add an element at a SPECIFIED INDEX
player.insert(0, "David")

# .extend()  -> Add ALL elements of another list into the current list
player.extend(sub_player)

print(f"List after adding players: {player}")


# ==============================================================================
# 3. DELETE 
# ==============================================================================
# .remove()  -> Delete the FIRST occurrence of a specified value
# player.remove("Harry")

# .pop()     -> Remove and return the element at a SPECIFIED INDEX (Default is the last item)
# removed_item = player.pop(1)

# del        -> Keyword to delete an item at an index or delete the entire list
# del player[0]


# ==============================================================================
# 4. SEARCH & UTILITIES
# ==============================================================================
# .index()   -> Return the index of the FIRST matched value
print(f"Index of Amad: {player.index('Amad')}")

# .count()   -> Return the number of times a specified value appears in the list
print(f"Count of Bruno: {player.count('Bruno')}")

# .copy()    -> Return a shallow copy of the list (creates a new object in memory)
player_copy = player.copy()


# ==============================================================================
# 5. LIST OPERATORS 
# ==============================================================================
# Operator + -> Concatenate (combine) two lists into a new third list
combined_list = player + sub_player

# Operator * -> Repeat (loop) the elements of the list N times
repeated_list = sub_player * 2


# ==============================================================================
# 6. SORT & REVERSE (Sắp xếp và Đảo ngược mảng)
# ==============================================================================
# .sort()    -> IN-PLACE SORT. Sorts the original list directly and returns None
# (Mặc định là sắp xếp tăng dần theo bảng chữ cái hoặc chữ số)
player.sort() 
# player.sort(reverse=True)  # Sắp xếp giảm dần trực tiếp

# sorted()   -> Returns a NEW sorted list, leaving the original list unchanged
# (Rất hữu ích khi muốn giữ nguyên mảng gốc để làm việc khác)
new_sorted_list = sorted(sub_player)

# .reverse() -> IN-PLACE REVERSE. Reverses the elements of the list directly
sub_player.reverse()


# ==============================================================================
# 7. ZIP FUNCTION 
# ==============================================================================
# zip()      -> Combine multiple lists into pairs (stops at the shortest list)
scores = [85, 90, 78]

# Application 1: Parallel loop 
for name, score in zip(player, scores):
    print(f"Player: {name} has score: {score}")

# Application 2: Quick Dictionary Mapping 
player_stats = dict(zip(player, scores))
print(f"Mapped Dictionary: {player_stats}")


# ==============================================================================
# 8. ENUMERATE FUNCTION 
# ==============================================================================
# enumerate() -> Return both the index and the value of items during a loop

# Application 1: Basic loop with index
for index, name in enumerate(player):
    print(f"Index: {index} - Player: {name}")

# Application 2: Change the start index 
for rank, name in enumerate(player, 1):
    print(f"Top {rank}: {name}")


# ==============================================================================
# 9. LIST COMPREHENSION
# ==============================================================================
# Normal way
num_list = [3, 4, 5, 6, 7, 8]

def square(data):
    square_list = []
    for num in data:
        square_num = num**2
        square_list.append(square_num)
    return square_list

print(square(num_list))

# Use comprehension
def square_comp(data):
    square_list = [value**2 for value in data]
    return square_list

print(square_comp(num_list))