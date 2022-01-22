# finding all the anagrams in a string
class Solution:
    def findAnagrams(self, s, p):
        # we ret [] if len of p > s
        if len(p) > len(s):
            return []

        pCount, sCount = {}, {}
        for i in range(len(p)):
            # we add that char in the hash map
            # if the char is not in the hash map, we get error
            # so we use get to give a default value 0 to the char in the hash map
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

        res = [0] if sCount == pCount else []
        # let left l = 0
        l = 0
        # including only the remaing elements
        for r in range(len(p), len(s)):
            # storing the element and increment in hash map
            sCount[s[r]] = 1 + sCount.get(s[r], 0)

            # removing the left element as we move towards right
            sCount[s[l]] -= 1

            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1

            # if the 2 hash map are equal then append in the list
            if sCount == pCount:
                res.append(l)

        return res


print(Solution().findAnagrams("abchrkldfbcaesdf", "abc"))
