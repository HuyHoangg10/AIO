def max_sliding_window(num_list: list, k: int) -> list:
    result_list = []
    for i in range(len(num_list) - k + 1):
        max_num = max(num_list[i:i+k])
        result_list.append(max_num)
        # print(i)

    return result_list


num_list_1 = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k_1 = 3
print(max_sliding_window(num_list_1, k_1))
