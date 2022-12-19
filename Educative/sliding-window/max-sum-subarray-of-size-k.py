def max_sum_subarray_size_k(arr, k):
    max_sum = 0

    for i in range(len(arr) - k + 1):
        window_sum = 0

        for j in range(i, i+k):
            window_sum += arr[j]

        max_sum = max(max_sum, window_sum)

    return max_sum
# time O(n2)


def solution2(arr, k):
    max_sum, window_sum = 0, 0
    start = 0

    for end in range(len(arr)):
        # add next element
        window_sum += arr[end]
        # slide till we reach k
        if end >= k-1:
            max_sum = max(max_sum, window_sum)
            # remove the start element
            window_sum -= arr[start]
            # move the start forward
            start += 1

    return max_sum


print(solution2([2, 1, 5, 1, 3, 2], 3))
