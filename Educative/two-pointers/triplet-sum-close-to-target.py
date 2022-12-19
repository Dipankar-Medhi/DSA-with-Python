import math


def tripletSumCloseToTarget(arr, target_sum):
    arr.sort()
    smallest_diff = math.inf

    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            target_diff = target_sum - arr[i] - arr[left] - arr[right]

            if target_diff == 0:  # exact triplet
                return target_sum - target_diff

            if (
                abs(target_diff) < abs(smallest_diff)
                or (abs(target_diff) == abs(smallest_diff))
                and target_diff
            ):
                smallest_diff = target_diff  # save closest and biggest diff

            if target_diff > 0:
                left += 1  # we need triplet with bigger sum
            else:
                right -= 1  # we need triplet with smaller sum

    return target_sum - smallest_diff


print(tripletSumCloseToTarget([1, 1, 1, 0], -100))
