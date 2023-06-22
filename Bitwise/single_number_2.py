""" 
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Example 1:
Input: [2,2,3,2]
Output: 3
"""


def singleNumber(nums):
    result = 0
    for i in range(32):
        count = 0
        for num in nums:
           
