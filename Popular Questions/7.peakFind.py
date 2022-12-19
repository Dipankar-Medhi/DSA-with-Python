"""
Given a non-empty array of integers arr, create a function that returns the index of a peak elements. We consider an element as peak if it's greater than or equal to its neighbors, the next and previus element, and the first element have at most one neighbor only. And if there are multiple peaks in arr, just return the index of one of them.
"""

# Binary Search - O(logn) time & space O(1)
# cause question asks to return one of the peak, not the greatest peak
# ------------------------------------------ #

# If the mid < mid + 1, left = mid,
# if mid > mid + 1, right = mid,
# do this untill left = right,
# return left, cause it will be at the peak

# ------------------------------------------ #


def findPeak(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right)//2
        # the element will be on the right half
        if arr[mid] < arr[mid + 1]:
            right = mid
        # on the left half
        else:
            left = mid + 1
    # at this point left and right will be equal
    return left

# Using recursion --- time O(logn)


def findPeakRec(arr, left, right):
    if left >= right:
        return left
    mid = (left + right)//2
    if arr[mid] < arr[mid + 1]:
        return findPeakRec(arr, mid+1, right)
    else:
        return findPeakRec(arr, left, mid)


def findPeak2(arr):
    return findPeakRec(arr, 0, len(arr)-1)


print(findPeak([1, 5, 8, 8, 3, 9]))
print(findPeak2([1, 5, 8, 8, 3, 9]))
