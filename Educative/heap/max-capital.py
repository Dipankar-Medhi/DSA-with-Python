import heapq


def findMaxCapital(capitals, profits, num_of_projects, initialcapital):
    minHeap = []
    maxHeap = []

    # store all project capitals in a min heap
    for i in range(len(capitals)):
        heapq.heappush(minHeap, (capitals[i], i))

    print("MinHeap:", minHeap)

    availablecapital = initialcapital
    for _ in range(num_of_projects):
        # find projects that can be selected with available capital and insert to maxHeap
        while minHeap and minHeap[0][0] <= availablecapital:
            capital, i = heapq.heappop(minHeap)
            heapq.heappush(maxHeap, (-profits[i], i))

        # if can't find
        if not maxHeap:
            break

        # select project with max profit
        profit, i = heapq.heappop(maxHeap)
        availablecapital += -profit

    return availablecapital


print(findMaxCapital([0, 1, 2, 3], [1, 2, 6, 5], 3, 0))
