"""
Problem Statement
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
"""
# Time O(n) | Space O(1)


def maxSubarr(arr, k):
    maxSum = 0
    windowSum = 0
    start = 0       # starting index of arr

    for i in range(len(arr)):
        windowSum += arr[i]

        if i >= k-1:
            maxSum = max(maxSum, windowSum)
            windowSum -= arr[start]
            start += 1

    return maxSum


print(maxSubarr([2, 1, 5, 1, 3, 2], 3))
