class Solution:
    def getConcatenation(self, nums):
        ans = [nums[i] for i in range(0, len(nums))]
        for j in range(0, len(nums)):
            ans.append(nums[j])

        return ans
