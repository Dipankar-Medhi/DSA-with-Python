def bubbleSort(arr):
    # to check if there is no swapping occuring in the 1st iteration i.e our arr is already sorted, we break the loop
    swapped = False
    # running for n-1 times
    for i in range(len(arr)):
        # for each step, max element comes at the last respective index
        # len(arr) - i is done cause with every iteration, the last item get sorted, so there is no need of reiterating once again through those elements.
        for j in range(1, len(arr)-i):
            # swap if the item is smaller than the previous item
            if (arr[j] < arr[j-1]):
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swapped = True
        # if swapped is false, i.e our arr is sorted, we break
        if (swapped == False):
            break

    return arr


arr = [3, 1, 5, 4, 2]
print(bubbleSort(arr))
