def reverse_array(arr, start, end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

    # or
    # while start < end:
    #   arr[start], arr[end] = arr[end], arr[start]
    # start += 1
    # end -= 1


def rotate_array(arr, n):
    # if n > len(arr) or n is -ve
    n = n % len(arr)
    if n < 0:
        # cal positive rotations needed.
        n = n + len(arr)
    # partition the arr
    # 1st reverse the whole array
    reverse_array(arr, 0, len(arr) - 1)
    # 2nd reverse the 0 to n - 1 part
    reverse_array(arr, 0, n - 1)
    # 3rd reverse the remaining part
    reverse_array(arr, n, len(arr) - 1)

    return arr


print(rotate_array([1, 10, 20, 0, 59, 63, 20, 9, 40], 2))
