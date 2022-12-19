def find_LIS_length(nums):
    n = len(nums)
    dp = [1 for _ in range(n)]

    maxLength = 1
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] <= dp[j]:
                dp[i] = dp[j] + 1
                maxLength = max(maxLength, dp[i])
    return maxLength


print(find_LIS_length([4, 2, 3, 6, 10, 1, 12]))
# O(n2) time | o(n) space
