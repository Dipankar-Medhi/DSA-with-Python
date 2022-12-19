"""
Input: {1, 2, 7, 1, 5}
Output: 0
Explanation: We can partition the given set into two subsets where minimum absolute difference 
between the sum of number is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.
"""


def minimum_difference(nums):
    n = len(nums)
    s = sum(nums)
    dp = [[False for _ in range(s//2 + 1)] for _ in range(n)]

    # make 1st column true
    for i in range(n):
        dp[i][0] = True

    # 1st row can be true if 1st element is equal to sum
    for j in range(1, s//2 + 1):
        if nums[0] == j:
            dp[0][j] = True

    # process the rest
    for i in range(1, n):
        for j in range(1, s//2 + 1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= nums[i]:
                dp[i][j] = dp[i - 1][j - nums[i]]

    # find the largest index in the last row which is true
    sum1 = 0
    i = s//2
    while i >= 0:
        if dp[n - 1][i] == True:
            sum1 = i
            break
        i -= 1

    sum2 = sum(nums) - sum1
    return abs(sum2 - sum1)


print(minimum_difference([1, 2, 7, 1, 5]))
