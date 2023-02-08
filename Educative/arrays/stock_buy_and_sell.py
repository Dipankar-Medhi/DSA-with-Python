def stock(prices):
    maxProfit = 0
    min_buy_price = prices[0]

    for i in range(len(prices)):
        min_buy_price = min(min_buy_price, prices[i])
        # we sell on the same day
        profit = prices[i] - min_buy_price
        maxProfit = max(profit, maxProfit)

    return maxProfit


# or
def max_profit(prices):
    n = len(prices)
    min_price = float("inf")
    max_profit = 0
    for i in range(n):
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            max_profit = max(max_profit, prices[i] - min_price)
    return max_profit


print(stock([7, 1, 5, 3, 6, 4]))

print(max_profit([7, 1, 5, 3, 6, 4]))
