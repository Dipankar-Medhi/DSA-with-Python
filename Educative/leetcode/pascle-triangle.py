def pascalTriangle(n):
    result = [[1], [1, 1]]

    for _ in range(n - 2):
        temp = []
        curr = result[-1]  # [1,1]
        temp.append(curr[0])

        j = 0
        while j < len(curr) - 1:
            s = 0
            s += curr[j] + curr[j + 1]
            temp.append(s)
            j += 1

        temp.append(curr[-1])

        result.append(temp)

    return result


print(pascalTriangle(5))
