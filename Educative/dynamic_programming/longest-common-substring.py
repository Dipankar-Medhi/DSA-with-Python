"""
Since we want to match all the substrings of the given two strings, we can use a two-dimensional array to store our results. The lengths of the two strings will define the size of the two dimensions of the array. So for every index ‘i’ in string ‘s1’ and ‘j’ in string ‘s2’, we have two options:

If the character at s1[i] matches s2[j], the length of the common substring would be one plus the length of the common substring till i-1 and j-1 indexes in the two strings.
If the character at the s1[i] does not match s2[j], we don’t have any common substring.

if s1[i] == s2[j] 
  dp[i][j] = 1 + dp[i-1][j-1]
else 
  dp[i][j] = 0 
"""


def longestCommonSubstring(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

    maxLen = 0

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                maxLen = max(maxLen, dp[i][j])

    print(maxLen)


print(longestCommonSubstring("passport", "ppsspt"))
