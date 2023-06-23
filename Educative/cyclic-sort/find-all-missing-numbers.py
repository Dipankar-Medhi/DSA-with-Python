def findAllMissingNumbers(arr):
    i = 0

    # sort the arr
    while i < len(arr):
        # correct index
        j = arr[i] - 1  # numbers are 1 to n
        
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    missingNumbers = []

    for i in range(len(arr)):
        if arr[i] != i + 1:
            missingNumbers.append(i + 1)

    return missingNumbers


arr = [2, 3, 1, 8, 2, 3, 5, 1]
print("Missing Numbers are: ", findAllMissingNumbers(arr))

# Time O(n)
