def find_target_subsets(num, s):
    totalSum = sum(num)

    if totalSum < s or (s + totalSum) % 2 == 1:
        return 0

    return count_subsets(num, int((s + totalSum) / 2))


def count_subsets(num, sum):
    n = len(num)
    dp = [[0 for _ in range(sum + 1)] for _ in range(n)]

    # we will always have an empty set for 0 sum
    for i in range(0, n):
        dp[i][0] = 1

    # we can form sum if num is equal to sum
    for i in range(1, sum + 1):
        dp[0][i] = 1 if num[0] == i else 0

    print(dp)

    for i in range(1, n):
        for j in range(1, sum + 1):
            dp[i][j] = dp[i - 1][j]  # we can always form prev sum
            if j >= num[i]:
                dp[i][j] += dp[i - 1][j - num[i]]
    print(dp)
    return dp[n - 1][sum]


print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))
