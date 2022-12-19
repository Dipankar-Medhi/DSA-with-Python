def find_max_in_bitonic(arr):
    start, end = 0, len(arr) - 1

    while start < end:
        mid = start + (end - start)//2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1

    # at the end, start == end
    return arr[start]


print(find_max_in_bitonic([1, 3, 8, 12, 4, 2]))
