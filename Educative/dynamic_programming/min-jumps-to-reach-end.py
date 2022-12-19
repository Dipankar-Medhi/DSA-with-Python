import math


def count_min_jumps(jumps):
    n = len(jumps)
    # initialize with infinity, except the first index which should be zero as we
    # start from there
    dp = [math.inf for _ in range(n)]
    dp[0] = 0

    for start in range(n - 1):
        end = start + 1
        while end <= start + jumps[start] and end < n:
            dp[end] = min(dp[end], dp[start] + 1)
            end += 1
    print(dp)
    return dp[n - 1]


print(count_min_jumps([2, 1, 1, 1, 4]))
