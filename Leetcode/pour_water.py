import heapq

def pourWater(heights, volWater, volDrop):
    n = len(heights)
    for i in range(volWater):
        idx = drop_index(heights, volDrop)
        heights[idx] += 1
    return heights

def drop_index(heights, volDrop):
    n = len(heights)
    left_heap = []
    right_heap = []
    
    idx = volDrop if heights[volDrop] == heights.index(min(heights)) else heights.index(min(heights))

    if idx == 0:
        heapq.heappush(right_heap, (heights[idx], idx))
    elif idx == n-1:
        heapq.heappush(left_heap, (-heights[idx], idx))
    else:
        heapq.heappush(left_heap, (-heights[idx], idx))
        heapq.heappush(right_heap, (heights[idx], idx))
    while left_heap and -left_heap[0][0] < heights[idx]:
        _, j = heapq.heappop(left_heap)
        heights[j] += 1
        if j < idx:
            idx = j
    while right_heap and right_heap[0][0] > heights[idx]:
        _, j = heapq.heappop(right_heap)
        heights[j] += 1
        if j > idx:
            idx = j

    return idx
    
print(pourWater([2,2,1,2,1,2,2], 4,3))