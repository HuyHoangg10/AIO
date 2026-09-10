sum = lambda x, y: x + y

print(sum(4, 5))

# More example

list1 = [4, 2, 9, 1, 5]
list2 = ["a", "b", "c", "d", "e"]

list3 = list(zip(list1, list2))


# normal way
def compare(item):
    return item[1]


print(f"list before sorted {list3}")

list4 = sorted(list3, key=compare, reverse=True)
print(f"list after sorted {list4}")

# using lambda
list5 = sorted(list3, key=lambda item: item[1], reverse=True)
print(f"list after sorted using lambda {list5}")


