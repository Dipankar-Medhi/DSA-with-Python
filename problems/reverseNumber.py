def reverseNum(num):
    n = num
    sum = 0
    while (n > 0):
        i = n % 10
        sum = (sum*10) + i
        n = n//10
    return (sum)


num = 12345
print(reverseNum(num))
