def findFirstKMissingPositiveNumbers(arr, k):
    n = len(arr)
    i = 0

    # cyclic sort
    while i < len(arr):
        # correct index
        j = arr[i] - 1
        # ignore negative and out of bounds num
        if arr[i] > 0 and arr[i] <= n and arr[i] != arr[j]:
            # swap them
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    print("Sorted arr: ", arr)

    missingNums = []
    extraNums = set()

    for i in range(n):

        if len(missingNums) < k:
            if arr[i] != i + 1:
                missingNums.append(i + 1)
                extraNums.add(arr[i])

    print(extraNums)

    # add the remaining missing numbers
    i = 1
    while len(missingNums) < k:
        candidateNum = i + n
        # ignore if extranum already has that number
        if candidateNum not in extraNums:
            missingNums.append(candidateNum)
        i += 1

    return missingNums


arr = [2, 1, 3, 6, 5]
print(findFirstKMissingPositiveNumbers(arr, 3))
