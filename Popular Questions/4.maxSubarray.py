"""
Given an array of integers arr, create a function that returns the
 sum of the subarray that has the greatest sum. And we don't 
consider the empty array as a subarray.
"""

# in subarray, elements must be contiguous block of elements of and array.


###########################################
# we either take the previus sum or not.
# depends on the sum. If sum is more, take it
# else leave it.

##########################################

# -------------------------------------- #
# Kadane's algorithm --- time O(n) space O(1)
# ---------------------------------------- #

from numpy import Infinity


def maxSubarray(arr):
    globalSum = -Infinity
    localSum = 0
    for element in arr:
        localSum = max(element, element + localSum)
        globalSum = max(globalSum, localSum)

    return globalSum


print(maxSubarray([2, 4, -8, 5, 3]))
