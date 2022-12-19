def ceiling_of_a_number(arr, key):
    start = 0
    end = len(arr) - 1
    # check if key is bigger than the biggest element in the arr
    if key > arr[end]:
        return -1

    while start <= end:
        mid = start + (end - start)//2

        if key < arr[mid]:
            end = mid - 1

        else:
            start = mid + 1

    # if loop ends, mean we are unable to find the key.
    # so the next big element must be start

    return start


print(ceiling_of_a_number([4, 6, 10, 15], 12))
