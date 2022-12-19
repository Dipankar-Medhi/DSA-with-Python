def backspace_compare(str1, str2):
    r1, r2 = "", ""

    i1, i2 = 0, 0

    while i1 < len(str1):
        if str1[i1] == "#":
            r1 = r1[0 : len(r1)]
            i1 += 1
        else:
            r1 += str1[i1]
            i1 += 1

    while i2 < len(str2):
        if str2[i2] == "#":
            r2 = r2[0 : len(r2)]
            i2 += 1
        else:
            r2 += str2[i2]
            i2 += 1
    print(r1, r2)
    if r1 == r2:
        return True
    return False


print(backspace_compare("##z", "z##"))
