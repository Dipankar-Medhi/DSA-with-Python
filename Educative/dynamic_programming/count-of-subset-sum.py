def count_of_subset_sum(nums, sum):
    n = len(nums)
    dp = [[0 for _ in range(sum + 1)] for _ in range(n)]
    print(dp)
    # 1st column == 0 can always be made with empty subarr
    for i in range(n):
        dp[i][0] = 1

    # and 1st row can be made with 1 element if it is equal to the sum
    for j in range(1, sum + 1):
        if nums[0] == j:
            dp[0][j] = 1

    for i in range(1, n):
        for j in range(1, sum + 1):
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i]]
    print(dp)
    return dp[n - 1][sum]


print(count_of_subset_sum([1, 1, 2, 3], 4))
