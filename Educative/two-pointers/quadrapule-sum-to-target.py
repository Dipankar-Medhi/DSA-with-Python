def search_quadruple(arr, target):
    arr.sort()
    quadruplets = []

    for i in range(len(arr) - 3):
        # skip duplicates
        if i > 0 and arr[i] == arr[i-1]:
            continue

        for j in range(i + 1, len(arr) - 2):
            # skip duplicates
            if j > 0 and arr[j] == arr[j - 1]:
                continue

            search_pairs(arr, target, i, j, quadruplets)

    return quadruplets


def search_pairs(arr, target, first, second, quadruplets):
    left = second + 1
    right = len(arr) - 1

    while left < right:
        sum = arr[first] + arr[second] + arr[left] + arr[right]
        if sum == target:
            quadruplets.append(
                [arr[first], arr[second], arr[left], arr[right]])

            left += 1
            right -= 1

            # skip same element to avoid duplicates
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif sum < target:
            left += 1  # we need bigger sum
        else:
            right -= 1  # we need smaller sum


print(search_quadruple([4, 1, 2, -1, 2, -3], 2))
