"""
X + Y + Z < target_sum
Y + Z < target_sum - X
"""

# time O(nlogn + n2) ~ O(n2)
# space O(n)


def tripletsWithSmallerSum(arr, target_sum):
    arr.sort()
    count = 0

    for i in range(len(arr) - 2):
        count += search(arr, target_sum - arr[i], i)

    return count


def search(arr, target_sum, first):
    count = 0
    left, right = first + 1, len(arr) - 1

    while left < right:
        if arr[left] + arr[right] < target_sum:
            count += right - left
            left += 1

        else:
            right -= 1
    return count


print(tripletsWithSmallerSum([-1, 0, 2, 3], 3))

# ------------------------------------------------ #
# return triplets

# time O(n3)
# space O(n)


def tripletsWithSmallerSum2(arr, target_sum):
    arr.sort()
    triplets = []
    for i in range(len(arr) - 2):
        search2(arr, target_sum - arr[i], i, triplets)

    return triplets


def search2(arr, target_sum, first, triplets):
    left, right = first + 1, len(arr) - 1

    while left < right:
        if arr[left] + arr[right] < target_sum:

            for i in range(right, left, -1):
                triplets.append([arr[first], arr[left], arr[i]])
            left += 1

        else:
            right -= 1


print(tripletsWithSmallerSum2([-1, 0, 2, 3], 3))
