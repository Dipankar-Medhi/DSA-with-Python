def search_rotated_arr(arr, key):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid

        # left part is sorted in ascending order
        if arr[start] <= arr[mid]:
            if key >= arr[start] and key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

        # right side is soted in ascending order
        else:
            if key > arr[mid] and key <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
    # not found
    return -1


print(search_rotated_arr([4, 5, 6, 7, 0, 1, 2], 0))


def search_rotated_with_duplicates(arr, key):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid

        # skip one number from start and end cause the start, end and mid could be the same
        if arr[start] == arr[mid] and arr[end] == arr[mid]:
            start += 1
            end -= 1
        # left side is sorted
        elif arr[start] <= arr[mid]:
            if key >= arr[start] and key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

        # right side is sorted
        else:
            if key > arr[mid] and key <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1


print("Position of key:", search_rotated_with_duplicates([1, 0, 1, 1, 1], 0))
