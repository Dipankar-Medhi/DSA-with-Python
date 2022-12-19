from collections import deque


def find_subarrays(arr, target):
    result = []
    product = 1
    left = 0
    # sliding window
    for right in range(len(arr)):
        product *= arr[right]

        while product >= target and left < len(arr):
            product /= arr[left]
            left += 1

        temp_list = deque()
        for i in range(right, left - 1, -1):
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))

    return result


print(find_subarrays([2, 5, 3, 10], 30))
