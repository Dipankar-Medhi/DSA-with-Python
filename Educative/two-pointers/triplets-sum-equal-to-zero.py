def search_triplet(arr):
    arr.sort()
    triplets = []

    for i in range(len(arr)):
        # skip duplicate elements
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        search_pair(arr, -arr[i], i + 1, triplets)

    return triplets


def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1

    while left < right:
        curr_sum = arr[left] + arr[right]

        if curr_sum == target_sum:
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1

            # skip duplicates
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif target_sum > curr_sum:
            left += 1
        else:
            right -= 1


print(search_triplet([-3, 0, 1, 2, -1, 1, -2]))
