def containsNearybyDuplicate(nums, k):
    start = 0

    result = False

    for end in range(len(nums)):

        if abs(start - end) <= k and nums[start] == nums[end] and start != end:
            result = True

        if abs(start - end) > k:
            start += 1

    return result


print(containsNearybyDuplicate([1, 2, 3, 1, 3], 2))
