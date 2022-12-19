import heapq


def find_kth_smallest(matrix, k):
    minHeap = []
    # put 1st element of each row in min heap
    # put min of k or len(matrix)
    for i in range(min(k, len(matrix))):
        heapq.heappush(minHeap, (matrix[i][0], 0, matrix[i]))

    # take smallest(top) element from min heap, if row
    # has more element, add next element to min heap
    numCount, num = 0, 0
    while minHeap:
        num, i, row = heapq.heappop(minHeap)
        numCount += 1
        if numCount == k:
            break
        # if there are more elements left, add to the min heap
        if len(row) > i + 1:
            heapq.heappush(minHeap, (row[i + 1], i + 1, row))
    return num


print(find_kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5))
