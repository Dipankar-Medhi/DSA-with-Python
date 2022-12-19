import math


def shortest_window_sort(arr):
    # find low and high respectivly
    low, high = 0, len(arr) - 1

    while low < len(arr) - 1 and arr[low] <= arr[low + 1]:
        low += 1
    # sorted array
    if low == len(arr) - 1:
        return 0

    while high > 0 and arr[high] >= arr[high - 1]:
        high -= 1

    subarr_max = -math.inf
    subarr_min = math.inf

    for k in range(low, high+1):
        subarr_max = max(subarr_max, arr[k])
        subarr_min = min(subarr_min, arr[k])

    # extend the subarr to include any number
    # bigger than minimum on the left side
    while low > 0 and arr[low - 1] > subarr_min:
        low -= 1

    # extend to include any number max than high
    while high < len(arr) - 1 and arr[high + 1] < subarr_max:
        high += 1

    return high - low + 1


print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
