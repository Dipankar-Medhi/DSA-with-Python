"""
Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
"""


def solution(arr, k):
    start, max_len, max_ones_count = 0, 0, 0

    for end in range(len(arr)):

        if arr[end] == 1:
            max_ones_count += 1
        # if zeroes become more than k
        if (end - start + 1 - max_ones_count) > k:
            if arr[start] == 1:
                max_ones_count -= 1
            start += 1

        max_len = max(max_len, end - start + 1)

    return max_len


print(solution([0, 1, 1, 0, 0, 0, 1, 1, 0], 2))
