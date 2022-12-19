"""
if st[endIndex] == st[startIndex] 
  dp[startIndex][endIndex] = 2 + dp[startIndex + 1][endIndex - 1]
else 
  dp[startIndex][endIndex] = Math.max(dp[startIndex + 1][endIndex], dp[startIndex][endIndex - 1])
"""


def longestPalindromicSubsequence(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # every sequence with one element is a palindrome
    for i in range(n):
        dp[i][i] = 1

    for startIndex in range(n - 1, -1, -1):
        for endIndex in range(startIndex + 1, n):
            # case 1: elements at the beginning and at the end are same
            if s[startIndex] == s[endIndex]:
                dp[startIndex][endIndex] = 2 + dp[startIndex + 1][endIndex - 1]
            else:  # case 2: skip one element either from beginning or end
                dp[startIndex][endIndex] = max(
                    dp[startIndex + 1][endIndex], dp[startIndex][endIndex - 1])

    return dp[0][n - 1]


print(longestPalindromicSubsequence("cddpd"))
