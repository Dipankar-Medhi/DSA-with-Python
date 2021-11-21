def subset(up, p):
    arr = []
    if up == "":
        return
    else:
        char = up[0]

        left = subset(up.replace(char, "", 1), p+char)
        right = subset(up.replace(char, "", 1), p)

        arr.append(left)
        arr.append(right)

        return arr


print(subset('abc', ''))
