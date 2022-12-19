def min_diff(arr, key):
    start, end = 0, len(arr) - 1

    if key < arr[start]:
        return arr[start]
    if key > arr[end]:
        return arr[end]

    while start <= end:
        mid = start + (end - start) // 2
        if key == arr[mid]:
            return arr[mid]

        if key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    # at the end of the loop, start == end + 1
    # return the closest of start and end
    if (arr[start] - key) < (key - arr[end]):
        return arr[start]
    return arr[end]


print(min_diff([1, 3, 8, 10, 15], 10))
