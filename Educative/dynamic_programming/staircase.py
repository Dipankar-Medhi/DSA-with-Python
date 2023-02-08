## Recursive solution
def count_ways(n):
    dp = [0 for i in range(n + 1)]
    return recurse(dp, n)


def recurse(dp, n):
    if n == 0:
        return 1

    if n == 1:
        return 1  # (1)
    if n == 2:
        return 2  # either (1,1) or (2)

    if dp[n] == 0:

        # if we take 1 step, thers 'n-1' step left
        take1step = recurse(dp, n - 1)
        # if we take 2 step, theres 'n - 2' step left
        take2step = recurse(dp, n - 2)
        take3step = recurse(dp, n - 3)

        dp[n] = take1step + take2step + take3step

    return dp[n]


print(count_ways(3))
# print("-" * 10)
# ## Bottom up
# def count_ways2(n):
#     # steps
#     dp = [0 for x in range(n + 1)]

#     dp[0] = 1
#     dp[1] = 1
#     dp[2] = 2

#     for i in range(3, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
#     print(dp)
#     return dp[n]


# print(count_ways2(3))
