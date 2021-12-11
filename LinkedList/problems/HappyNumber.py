def isHappy(n: int) -> bool:
    slow = n
    fast = findSquareSum(n)
    while fast != slow:
        slow = findSquareSum(slow)
        fast = findSquareSum(findSquareSum(fast))

    if fast == 1:
        return True

    else:
        return False


def findSquareSum(n):
    ans = 0
    while n > 0:
        rem = n % 10
        ans += rem * rem
        n = n // 10

    return ans


print(isHappy(19))

