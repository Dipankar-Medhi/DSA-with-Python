paths = []


def path(p, r, c):
    if r == 1 and c == 1:
        paths.append(p)

    if (r > 1):
        path(p+'D', r-1, c)
    if (c > 1):
        path(p+'R', r, c-1)

    return paths


# print(path("", 3, 3))

# diagonal paths included
newPahts = []


def incldiapath(p, r, c):
    if r == 1 and c == 1:
        newPahts.append(p)

    if r > 1 and c > 1:
        incldiapath(p+'D', r-1, c-1)

    if r > 1:
        incldiapath(p+'V', r-1, c)

    if c > 1:
        incldiapath(p+'H', r, c-1)

    return newPahts


print(incldiapath("", 3, 3))
