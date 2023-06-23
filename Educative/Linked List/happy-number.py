def findHappyNumber(num):
    slow, fast = num, num
    

    while True:
        slow = findSquare(slow)
        fast = findSquare(findSquare(fast))

        if slow == fast:
            break
    # if cycle meets at 1, then its a happy number
    return slow == 1


def findSquare(num):
    summ = 0

    while num > 0:
        digit = num % 10
        summ += digit ** 2
        num //= 10
    return summ


print(findHappyNumber(12))
print(findHappyNumber(23))
