def binary_search(arr, key):
    start = 0
    end = len(arr) - 1

    isAscending = arr[start] < arr[end]

    while start <= end:
        # find mid element
        mid = start + (end - start)//2

        if key == arr[mid]:
            return mid

        # ascending order
        if isAscending:
            if key < arr[mid]:
                # key is on the 1st half
                end = mid - 1
            else:
                # on second half
                start = mid + 1

        # descending order
        else:
            if key > arr[mid]:
                # key on 1st half
                end = mid - 1
            else:
                start = mid + 1

    return -1


print(binary_search([4, 5, 10], 10))
