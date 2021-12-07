'''
374. Guess Number Higher or Lower
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        start = 0
        end = n

        while start <= end:
            mid = int((start + end)//2)
            if guess(mid) < 0:
                end = mid - 1
            elif guess(mid) > 0:
                start = mid + 1
            else:
                return mid
