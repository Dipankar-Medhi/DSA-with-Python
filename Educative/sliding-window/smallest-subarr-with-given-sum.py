import math

def smallestSubarrWithGivenSum(s, arr):

    winSum = 0
    minLength = math.inf
    start = 0

    for end in range(len(arr)):
        # keep adding
        winSum += arr[end]
        # once the sum is >= given s
        while winSum >= s:
            # find the min length of the previous min length and current length
            minLength = min(minLength, end - start + 1)
            # also remove the start element
            winSum -= arr[start]
            # and move start forward
            start += 1

    if minLength == math.inf:
        return 0
    return minLength


minLenth = smallestSubarrWithGivenSum(7, [2, 1, 5, 2, 3, 2])
print(minLenth)

# time complexity is O(N + N) or O(N)
# space O(1)
