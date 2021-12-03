class Solution:
    def buildArray(self, nums):
        ans = [nums[nums[i]] for i in range(0, len(nums))]
        return ans
