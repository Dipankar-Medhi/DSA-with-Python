def min_coin_change(denominations, total):
    n = len(denominations)
    dp = [[0 for _ in range(total + 1)] for _ in range(n)]

    # 1st column == 0 cause 0 coins needed to make total of 0

    # 1st row require equal no of coins as of toatl if it is 1
    for j in range(1, total + 1):
        if denominations[0] == 1:
            dp[0][j] = j

    for i in range(1, n):
        for j in range(1, total + 1):

            dp[i][j] = min(dp[i - 1][j], dp[i][j - denominations[i]] + 1)
    print(dp)
    return dp[n - 1][total]


print(min_coin_change([1, 2, 3], 7))
