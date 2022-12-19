def find_least_common_number(a, b, c):
    i, j, k = 0, 0, 0

    while i < len(a) and j < len(b) and k < len(c):
        # found common num
        if a[i] == b[j] == c[k]:
            return a[i]

        # let's increment the smallest number row
        if a[i] <= b[j] and a[i] <= c[k]:
            i += 1

        elif b[j] <= a[i] and b[j] <= c[k]:
            j += 1

        elif c[k] <= a[i] and c[k] <= b[j]:
            k += 1

    return -1


v1 = [6, 7, 10, 25, 30, 63, 64]
v2 = [1, 4, 5, 6, 7, 8, 50]
v3 = [1, 6, 10, 14]

result = find_least_common_number(v1, v2, v3)
print("Least Common Number: " + str(result))
