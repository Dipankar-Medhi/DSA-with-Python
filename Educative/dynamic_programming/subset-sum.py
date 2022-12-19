"""
Input: {1, 2, 3, 7}, S=6
Output: True
The given set has a subset whose sum is '6': {1, 2, 3}
"""


def can_partition(num, sum):
    n = len(num)
    dp = [[False for x in range(sum+1)] for y in range(n)]

    # 1st column, sum == 0 column, we can always form sum == 0 with empty subarr
    for i in range(n):
        dp[i][0] = True

    # we can for sub arr with one number is element is equal to its sum
    for j in range(1, sum+1):
        if num[0] == j:
            dp[0][j] = True

    # process the rest
    for i in range(1, n):
        for j in range(1, sum + 1):
            # if we can have sum with including the number at index i
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i - 1][j - num[i]]
    print(dp)
    return dp[n-1][sum]


print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
