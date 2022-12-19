import math


def find_min_visits(intervals):
    intervals.sort(key=lambda x: x[1])
    print("Sorted intervals:", intervals)

    prev, count = -math.inf, 0
    for interval in intervals:
        if interval[0] > prev:
            prev = interval[1]
            count += 1

    return count


print(find_min_visits([[1, 2], [2, 3], [3, 4], [2, 3], [3, 4], [4, 5]]))

# time O(nlogn)
