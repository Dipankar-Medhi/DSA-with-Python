def find_LPS_length(s):
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]

    # every string with one character is a palindrome
    for i in range(n):
        dp[i][i] = True

    maxLength = 1
    for start in range(n - 1, -1, -1):
        for end in range(start + 1, n):
            if s[start] == s[end]:
                if end - start == 1 or dp[start + 1][end - 1]:
                    dp[start][end] = True
                    maxLength = max(maxLength, end - start + 1)

    return maxLength


print(find_LPS_length("abdbca"))
# O(n2) time
