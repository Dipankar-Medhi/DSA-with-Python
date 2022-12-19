def move_zeores_to_left(arr):
    if len(arr) < 1:
        return

    n = len(arr)
    read = n - 1
    write = n - 1

    while read >= 0:
        if arr[read] != 0:
            arr[write] = arr[read]
            write -= 1

        read -= 1
    # read finishes, but write index remains
    # make the remaining elements zeroes
    while write >= 0:
        arr[write] = 0
        write -= 1

    return arr


print(move_zeores_to_left([1, 10, 20, 0, 50, 60, 0, 80, 0]))
