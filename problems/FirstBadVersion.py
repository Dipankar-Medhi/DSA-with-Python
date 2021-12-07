class Solution:
    def isBadVersion(self, n):
        if n >= 4:
            return True
        else:
            return False

    def firstBadVersion(self, n):
        s = 1
        e = n
        while (s < e):
            pivot = (s+e) // 2
            if (self.isBadVersion(pivot)):
                e = pivot       # keep track of the leftmost bad version
            else:
                s = pivot + 1   # the one after the rightmost good version
        return s


print(Solution().firstBadVersion(5))
