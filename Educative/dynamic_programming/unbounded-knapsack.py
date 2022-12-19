def solveKnapsack(profits, weights, capacity):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(profits))]

    for i in range(1, capacity + 1):
        if weights[0] <= i:
            dp[0][i] = profits[0] * i

    print(dp)

    for i in range(1, len(profits)):
        for j in range(1, capacity + 1):
            if weights[i] > j:
                dp[i][j] = dp[i - 1][j]
            elif weights[i] <= j:
                dp[i][j] = max(dp[i - 1][j], profits[i] + dp[i][j - weights[i]])

    return dp[len(profits) - 1][capacity]


print(solveKnapsack([15, 50, 60], [1, 3, 4], 8))
