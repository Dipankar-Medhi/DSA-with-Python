import heapq


def fidn_kth_smallest_number(nums, k):
    maxHeap = []
    # put first k numbers in the max heap
    for i in range(k):
        heapq.heappush(maxHeap, -nums[i])

    # for remaining elements, if it is smaller than top element of the heap,
    # remove the top and add the number in the heap

    for i in range(k, len(nums)):
        if -nums[i] > maxHeap[0]:
            heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, -nums[i])
    print(maxHeap)
    # the root will have the kth smallest element
    return -maxHeap[0]


print(fidn_kth_smallest_number([1, 5, 12, 2, 11, 5], 3))

# time O(nlogk)
