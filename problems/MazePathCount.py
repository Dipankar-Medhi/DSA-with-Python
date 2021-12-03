def mazePathCount(row, col):
    if (row == 1 or col == 1):
        return 1

    left = mazePathCount(row - 1, col)
    right = mazePathCount(row, col - 1)

    return left + right


print(mazePathCount(3, 3))
