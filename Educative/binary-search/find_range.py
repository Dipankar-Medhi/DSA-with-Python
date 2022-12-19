def find_range(arr, key):
    result = [-1, -1]

    result[0] = binary_search(arr, key, False)
    # no need to search if 1st element is not found
    if result[0] != -1:
        result[1] = binary_search(arr, key, True)
    return result


def binary_search(arr, key, findMaxIndex):
    start = 0
    end = len(arr) - 1
    keyIndex = -1

    while start <= end:
        mid = start + (end - start) // 2

        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:  # key == arr[mid]
            keyIndex = mid
            # to find last index
            if findMaxIndex:
                start = mid + 1  # move the pointer forward to find last index
            else:
                end = mid - 1  # move the pointer backward to find first index of key
    return keyIndex


print(find_range([4, 6, 6, 6, 9], 6))

# time O(logn)
# space O(1)
