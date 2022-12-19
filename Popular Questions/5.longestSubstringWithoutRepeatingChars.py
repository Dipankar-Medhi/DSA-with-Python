"""
Given a string str made of alphabetical letters only, create a function that returns the length of the longest substring without repearing charactres.
"""
# Brute force solution:
# check all substrings while keeping track of the longest one
# that has no repeating chars

# ----------------------------------------- #

# ASCII chars:
# A to Z ---> 65 to 90
# a to z ---> 97 to 122

# ----------------------------------------- #

# time O(n3) space O(1)


from turtle import st

from sympy import Indexed


def withoutRepeating(str):
    # all false elements
    visited = [False]*128
    # for each char
    for char in str:
        if visited[ord(char)]:
            return False
        else:
            visited[ord(char)] = True
    return True


def longestSubstringWithoutRepeating(str):
    maxlen = 0
    for i in range(len(str)):
        for j in range(i, len(str)):
            substr = str[i:j+1]
            if withoutRepeating(substr) and len(substr) > maxlen:
                maxlen = len(substr)
    return maxlen

# time O(n) & space O(1)


def longestSubstringWithoutRepeating2(str):
    maxlength = 0
    start = 0
    indexes = [-1]*128

    for i in range(len(str)):
        # if not -1 or > -1
        if indexes[ord(str[i])] >= start:
            start = indexes[ord(str[i])] + 1
        # replace the unicode position with char
        indexes[ord(str[i])] = i
        maxlength = max(maxlength, i - start + 1)
    return maxlength


print(longestSubstringWithoutRepeating2('apple'))
