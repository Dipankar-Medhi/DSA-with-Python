def findCorruptPair(arr):
    i = 0
    while i < len(arr):
        j = arr[i] - 1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    print(arr)
    for i in range(len(arr)):
        if arr[i] != i + 1:
            return [arr[i], i + 1]

    return [-1, -1]


arr = [3, 1, 2, 5, 2]
print(findCorruptPair(arr))
