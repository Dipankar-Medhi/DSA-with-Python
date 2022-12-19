"""
arr from 0 to maxIndex is increasing and maxIndex + 1 to end is decreasing.
So we can search in the both arr separetly."""


def search_bitonic_arr(arr, key):
    maxIndex = findMax(arr)
    keyIndex = binary_search(arr, key, 0, maxIndex)
    if keyIndex != -1:
        return keyIndex
    return binary_search(arr, key, maxIndex + 1, len(arr) - 1)


# find the max value in bitonic arr
def findMax(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1

    return start


# binary search


def binary_search(arr, key, start, end):
    while start <= end:
        mid = int(start + (end - start) // 2)

        if key == arr[mid]:
            return mid
        # ascending part
        if arr[start] < arr[end]:
            if key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:  # descending part
            if key > arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

    return -1


print(search_bitonic_arr([1, 3, 8, 4, 3], 4))
print("Max element is at:", findMax([3, 4, 5, 1, 2]))
