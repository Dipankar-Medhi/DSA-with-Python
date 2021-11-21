def insertionSort(arr):
    # outer loop
    for i in range(len(arr)-1):
        # j is always i + 1
        j = i + 1
        # internal loop for j>0 and j moves from right to left
        while(j > 0):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j = j - 1
            # if j = 0, we break the internal loop
            else:
                break
    return arr


arr = [5, 4, 1, 3, 2]
print(insertionSort(arr))
