# sample_data = [64, 34, 25, 12, 22, 11, 90]


# def bubble_sort_optimize(arr):
#     for i in range(len(arr)-1):
#         swapped = False
#         for j in range(len(arr) - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#         if not swapped:
#             break
#     return arr


# sorted_data = bubble_sort_optimize(sample_data)
# print(sorted_data)


# cart_items = [
#     ("Laptop", 1200, 1),
#     ("Mouse", 25, 4),
#     ("Keyboard", 75, 2),
#     ("Headphones", 150, 3)
# ]
# sorted_cart_items = sorted(cart_items,key=lambda item:item[1]*item[2],reverse=True)


numbers = [2, 3, 4, 10, 40]
search_value = 10


def binary_search(list_data, search_value):
    low = 0
    high = len(list_data) - 1
    while low <= high:
        mid = (low + high) // 2
        if list_data[mid] == search_value:
            return mid
        elif list_data[mid] < search_value:
            low = mid + 1
        else:
            high = mid - 1
    return -1


print(binary_search(numbers, search_value))
