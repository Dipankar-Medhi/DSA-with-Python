def find_low_high_index(arr, key):

    low = binary_search(arr, key, True)
    high = binary_search(arr, key, False)

    return (low, high)


def binary_search(arr, key, findLow):
    start = 0
    end = len(arr) - 1
    index = -1
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] < key:
            start = mid + 1
        elif arr[mid] > key:
            end = mid - 1
        else:
            index = mid

            if findLow:
                end = mid - 1
            else:
                start = mid + 1

    return index


print(find_low_high_index([1, 5, 5, 5, 6, 7], 5))
