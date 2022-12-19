## Recursive solution
def count_ways(n):
    if n == 0:
        return 1

    if n == 1:
        return 1  # (1)
    if n == 2:
        return 2  # either (1,1) or (2)

    # if we take 1 step, thers 'n-1' step left
    take1step = count_ways(n - 1)
    # if we take 2 step, theres 'n - 2' step left
    take2step = count_ways(n - 2)
    take3step = count_ways(n - 3)

    return take1step + take2step + take3step


print(count_ways(3))
print("-" * 10)
## Bottom up
def count_ways2(n):
    # steps
    dp = [0 for x in range(n + 1)]

    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    print(dp)
    return dp[n]


print(count_ways2(3))
