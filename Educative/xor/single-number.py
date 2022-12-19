def findSingleNumber(arr):
    num = 0
    for i in arr:
        num ^= i

    return num


arr = [1, 2, 1, 2, 4, 5, 4]
print(findSingleNumber(arr))
