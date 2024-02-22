def find_max_sum_sub_array(k, arr):
    n = len(arr)
    max_sum = sum(arr[:k])
    present_sum = max_sum
    for i in range(k, n):
        present_sum = present_sum + arr[i] - arr[i-k]
        max_sum = max(max_sum, present_sum)
    return max_sum

if __name__ == '__main__':
    print(find_max_sum_sub_array(3, [2, 1, 5, 1, 3, 2])) # 9
    print(find_max_sum_sub_array(2, [2, 3, 4, 1, 5])) # 7
    print(find_max_sum_sub_array(2, [2, 1, 4, 1, 1])) # 5
    print(find_max_sum_sub_array(3, [2, 1, 4, 1, 1])) # 7
    print(find_max_sum_sub_array(4, [2, 1, 4, 1, 1])) # 8