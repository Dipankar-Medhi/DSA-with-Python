# to check if the words match
def isMatching(left, text, pattern):
    res = None
    for i in range(len(pattern)):
        # index < than the len of text
        if left+i < len(text):
            if text[left+i] == pattern[i]:
                res = True
            else:
                res = False
    return res


def findPatternPosition(text, pattern):
    # incase len of pattern > text
    if len(pattern) > len(text):
        return [-1, -1]

    left = 0

    res = [0] if isMatching(left, text, pattern) else []

    # add 1 element to the left --> i.e slide one element
    for i in range(left + 1, len(text)):
        if left < len(text):
            if isMatching(i, text, pattern):
                res.append(i)
                left += 1
            else:
                left += 1
    return res


# print(isMatching(6, "abcpqrabc", "abc"))
print(findPatternPosition("abcpqrabcefgabc", "abc"))
