def findAvgSumOfSubarr(k, arr):
    result = []

    sum, start = 0.0, 0

    for end in range(len(arr)):
        sum += arr[end]  # keep adding the elements

        # once the len of arr reaches k
        if end >= k - 1:
            # add to the result
            result.append(sum/k)
            # then remove the element going out from the arr
            sum -= arr[start]
            # and move the start by 1 place
            start += 1

    return result


avgSum = findAvgSumOfSubarr(5, [1, 3, 4, -1, 4, 6, 8])
print(avgSum)
