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

# --------------------------------------------------- #
# top down
def count_min_jumps2(jumps):
    dp = [0 for x in range(len(jumps))]
    return recurse(dp, jumps, 0)


def recurse(dp, jumps, i):
    n = len(jumps)

    # reached end
    if jumps[i] == n - 1:
        return 0

    if jumps[i] == 0:
        return math.inf

    # already has the solution
    if dp[i] != 0:
        return dp[i]

    totalJumps = math.inf
    s, e = i + 1, i + jumps[i]

    while s < n and s <= e:
        minJumps = recurse(dp, jumps, s)
        s += 1

        if minJumps != math.inf:
            totalJumps = min(totalJumps, minJumps + 1)

    dp[i] = totalJumps
    return dp[i]


print("Top down:", count_min_jumps2([2, 1, 1, 1, 4]))
