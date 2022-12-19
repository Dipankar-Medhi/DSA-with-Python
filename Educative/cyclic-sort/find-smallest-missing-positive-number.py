def findSmallestMissingPositiveNumber(arr):
    i = 0

    # cyclic sort
    while i < len(arr):
        # corect index
        j = arr[i] - 1
        # ignoring all negative numbers and all numbers greater than or equal to the length of the array
        if arr[i] > 0 and arr[i] <= len(arr) and arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    print(arr)
    for i in range(len(arr)):
        if arr[i] != i + 1:
            return i + 1

    return len(arr) + 1


arr = [-3, 1, 5, 4, 2]
print(findSmallestMissingPositiveNumber(arr))
