""" 
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share any common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".

"""
def maxProduct(words):
    n = len(words)
    bit_rep = [0] * n
    for i in range(n):
        for c in words[i]:
            bit_rep[i] |= 1 << (ord(c) - ord('a'))
    max_product = 0
    for i in range(n):
        for j in range(i + 1, n):
            if bit_rep[i] & bit_rep[j] == 0:
                max_product = max(max_product, len(words[i]) * len(words[j]))
    return max_product

words = ["abcw","baz","foo","bar","xtfn","abcdef"]
print(maxProduct(words))