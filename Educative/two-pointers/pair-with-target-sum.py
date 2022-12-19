def pairWithTargetSum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        # we need less sum
        if (arr[left] + arr[right]) > target:
            right -= 1
        # we need more sum
        if (arr[left] + arr[right]) < target:
            left += 1
        if (arr[left] + arr[right]) == target:
            return [left, right]

    return [-1, -1]


print(pairWithTargetSum([1, 2, 3, 4,  6], 6))
