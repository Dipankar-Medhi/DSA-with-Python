"""
Given a string str, create a function that returns the first repearing character. If such char doesn't exist, return null char '\0'
"""

# Brute force ---- time O(n2)
# for each char, we check all the char before it to know if we have seen it before
# --- str = 'responsible', we keep moving forward till we meet s again after n,


def firstRepeatingChar(str):

    for i in range(len(str)):
        # check if it already exist in the previous chars
        for j in range(i):
            # if the char matches
            if str[i] == str[j]:
                return str[i]
    return '\0'


# we cannot sort --> it will break the order
# cause we need the 1st repeating char

# ----------------------- #

# Using hash table --- time O(n) & space O(n)
# we keep storing the char for the iteration and keep checking if it exist in the hash table

def firstRepeatingChar2(str):
    visited = {}
    for char in str:
        # keep storing char if not already present
        if visited.get(char):
            return char
        else:
            visited[char] = True
    return '\0'


print(firstRepeatingChar('responsible'))
print(firstRepeatingChar2('responsible'))
