def pascalTrianle(nrows):
    # 1st row
    res = [[1]]

    # skipping 1st row
    for _ in range(nrows - 1):
        # add [0] to left and right
        temp = [0] + res[-1] + [0]
        row = []

        # for each element inside res
        for i in range(len(res[-1]) + 1):
            row.append(temp[i] + temp[i + 1])

        # add to res
        res.append(row)
    return res


def generate(numRows):
    # initiate 1st row element
    res = [[1]]

    # skip 1st row, cause its already present (as res)
    for i in range(numRows - 1):
        # add 0 to start and finish to res's latest row (by res[-1])
        temp = [0] + res[-1] + [0]
        row = []

        for j in range(len(res[-1]) + 1):
            # add the elements and add to row
            row.append(temp[j] + temp[j+1])
            # finally add to res as the latest element
        res.append(row)
    return res


print(generate(5))
