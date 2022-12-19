def setZeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])

    # initialize 1st row not zero
    rowZero = False

    # for every rows and col
    for r in range(rows):
        for c in range(cols):
            # if an element is zero
            if matrix[r][c] == 0:
                # make the elements of 1st row zero
                matrix[0][c] = 0

                # turn 1st coln elements zero from 2nd row
                if r > 0:
                    matrix[r][0] = 0
                else:
                    rowZero = True

    # from 2nd row and cols
    for r in range(1, rows):
        for c in range(1, cols):
            # check if 1st row and 1st col elements are zero
            # if zero
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    # edge case
    # if 1st element is zero
    if matrix[0][0] == 0:
        # turn 1st row and col = 0
        for r in range(rows):
            matrix[r][0] = 0

    # if 1st row is zero
    if rowZero:
        for c in range(cols):
            matrix[0][c] = 0

    return matrix


print(setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
