def permutation(processed, unprocessed):

    if unprocessed == "":
        return processed

    char = unprocessed[0]
    for i in range(len(processed)):
        f = processed[0:i]
        s = processed[i:len(processed)]
        processed = f + char + s
        permutation(processed, unprocessed.replace(char, "", 1))


print(permutation("", "abc"))
