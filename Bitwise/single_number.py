"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Example:
Input: [2,2,1]
Output: 1
"""

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

nums = [1,2,2]

print(singleNumber(nums))