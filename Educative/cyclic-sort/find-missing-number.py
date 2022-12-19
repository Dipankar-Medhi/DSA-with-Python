def findMissingNumber(arr):
    i = 0
    n = len(arr)

    # sort the arr
    while i < n:
        # correct index
        j = arr[i]

        # swap
        if arr[i] < n and arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    print("Sorted arr: ", arr)

    # find the missing number from its index
    for i in range(n):
        if arr[i] != i:
            return i

    return n


arr = [4, 0, 3, 1]
print("Missing Number: ", findMissingNumber(arr))
