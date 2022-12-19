import heapq


def find_kth_smallest(lists, k):
    minHeap = []

    # put 1st element of each lisst in the minheap
    for i in range(len(lists)):
        heapq.heappush(minHeap, (lists[i][0], 0, lists[i]))

    # take top element(smallest) from minheap and keep counting
    count = 0

    while minHeap:
        number, i, list = heapq.heappop(minHeap)
        count += 1

        if count == k:
            break
        # put next element of the arr to minheap
        if len(list) > i + 1:
            heapq.heappush(minHeap, (list[i+1], i, list))

    return number


print(find_kth_smallest([[2, 6, 8], [3, 6, 7]], 5))
