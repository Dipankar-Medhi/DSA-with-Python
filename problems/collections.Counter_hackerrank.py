from collections import Counter

shoesNum = int(input())
# # shoesSize = Counter(input().split(" "))
# customers = int(input())

shoesPrice = []

prices = {}

for i in range(shoesNum):
    shoesPrice.append(input().split(" "))

prices = {j[0]: j[1:][0] for j in shoesPrice}


print(prices)
