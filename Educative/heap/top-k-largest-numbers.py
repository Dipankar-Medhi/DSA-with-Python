import heapq


def find_k_largest_numbers(nums, k):
    minHeap = []
    # put first k numbers in min heap
    for i in range(k):
        heapq.heappush(minHeap, nums[i])

    # for the rest of nums in arr, if a num is >> than top element of min heap, remove the top num from the heap and add the num
    for i in range(k, len(nums)):
        if nums[i] > minHeap[0]:
            heapq.heappop(minHeap)
            heapq.heappush(minHeap, nums[i])

    # the heap will have top k largest numbers
    return list(minHeap)


print(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3))

# Time O(Nlogk)
# space O(K)
