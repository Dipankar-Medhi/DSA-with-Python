"""
Problem Statement #
Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
"""

import math


def solution(arr, s):
    windowSum = 0
    minLength = math.inf
    start = 0

    for i in range(len(arr)):
        # add next element
        windowSum += arr[i]
        # shring the window until windowSum is < s
        while windowSum >= s:
            minLength = min(minLength, i - start + 1)
            windowSum -= arr[start]
            start += 1
    if minLength == math.inf:
        return 0
    return minLength


print(solution([2, 1, 5, 2, 3, 2], 7))
# --> 2
