from heapq import heappop, heappush


def longestConsecutive(nums) -> int:
    nums = list(set(nums))

    minHeap = []
    for i in range(len(nums)):
        heappush(minHeap, nums[i])

    print(minHeap)
    globalCount = 0
    count = 1

    while minHeap:
        num = heappop(minHeap)
        if minHeap and abs(num - minHeap[0]) == 1:
            count += 1
        else:
            count = 1
        globalCount = max(globalCount, count)

    return globalCount


print(longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))
