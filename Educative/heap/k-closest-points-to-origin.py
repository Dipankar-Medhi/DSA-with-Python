import heapq

# Time O(nlogk) and space O(k)
def find_dist(coordinate):
    x, y = coordinate
    return x * x + y * y


def find_closest_points(points, k):
    maxHeap = []

    for i in range(k):
        dist = find_dist(points[i])
        heapq.heappush(maxHeap, (-dist, points[i]))

    print(maxHeap)

    # for rest of the elements, if a point is closer to origin than the top of heap,
    # remove top element and add the point
    for i in range(k, len(points)):
        if find_dist(points[i]) < -maxHeap[0][0]:
            heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, (-find_dist(points[i]), points[i]))

    return list(maxHeap)


result = find_closest_points([(1, 3), (3, 4), (2, -1)], 2)

print("Closest points are:", result)
