def stock(prices):
    maxProfit = 0
    min_buy_price = prices[0]

    for i in range(len(prices)):
        min_buy_price = min(min_buy_price, prices[i])
        # we sell on the same day
        profit = prices[i] - min_buy_price
        maxProfit = max(profit, maxProfit)

    return maxProfit


print(stock([7, 1, 5, 3, 6, 4]))
