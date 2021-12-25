def mergeSort(array):
    # we check if the len of the array is 0 n 1, then we return the array
    if len(array) == 0 or len(array) == 1:
        return array

    # we first find the mid, then we split the arr into two half
    mid = len(array) // 2
    arr1 = array[0:mid]
    arr2 = array[mid:]

    # then we call the mergesort algo on the splitted parts recursively
    mergeSort(arr1)
    mergeSort(arr2)

    # Then the arrays are sorted and merged into the original array
    merge(arr1, arr2, array)

    # return the sorted array
    return array


# merge function
def merge(arr1, arr2, array):
    # initialising the indexes for traversal
    i, j, k = 0, 0, 0

    # while index is less tha the len of the splitted arrays
    while i < len(arr1) and j < len(arr2):
        # we sort the values of the two arrays, and merge the elemnets accordingly
        if arr1[i] < arr2[j]:
            array[k] = arr1[i]
            # if i value is < than j value, then we put i value in the array
            # then we increment the i to i +1, cause i is less than j
            # but i+ 1 might be > j, so we only increment the i and k value.
            k += 1
            i += 1
        else:
            # same method
            array[k] = arr2[j]
            k += 1
            j += 1
    # If one of the arr is fully traversed, and other half remains, then we add the other half to the array
    # say, j has reached the end of the arr2, so there are still values remained in the arrr1
    # so we add the remaining values of i arr, to the array.
    while i < len(arr1):
        array[k] = arr1[i]
        k += 1
        i += 1
    while j < len(arr2):
        array[k] = arr2[j]
        k += 1
        j += 1


print(mergeSort([12, 3, 7, 2, 9]))

