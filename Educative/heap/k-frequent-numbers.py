import heapq


def find_k_frequent_numbers(nums, k):

    # store the freq of nums in a hash map
    num_freq = {}
    for num in nums:
        num_freq[num] = num_freq.get(num, 0) + 1

    minHeap = []
    # push the nums in the heap and if heap size is >> k, remove the top most element(smallest)
    for num, freq in num_freq.items():
        heapq.heappush(minHeap, (freq, num))
        if len(minHeap) > k:
            heapq.heappop(minHeap)

    print(minHeap)

    # create a list of top k nums
    topNums = []
    while minHeap:
        # we need only the nums, no their freq
        topNums.append(heapq.heappop(minHeap)[1])

    return topNums


print(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2))
