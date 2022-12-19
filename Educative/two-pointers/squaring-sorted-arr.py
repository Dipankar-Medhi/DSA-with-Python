def make_square(arr):
    n = len(arr)
    squares = [0 for i in range(n)]
    largestSquare = n-1
    # two pointes - one at left end, one at right
    left, right = 0, n-1

    while left <= right:
        leftSquare = arr[left]**2
        rightSquare = arr[right]**2

        # adding the largest square to the result arr (at the end)
        if leftSquare > rightSquare:
            squares[largestSquare] = leftSquare
            left += 1
        else:
            squares[largestSquare] = rightSquare
            right -= 1
        largestSquare -= 1

    return squares


print(make_square([-2, -1, 0, 2, 3]))
