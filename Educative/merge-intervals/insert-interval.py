def insertInterval(intervals, newInterval):
    mergedIntervals = []
    # since there are only 2 elements in an interval, 0 and 1.
    i, start, end = 0, 0, 1

    # add all intervals that come before new interval
    while i < len(intervals) and intervals[i][end] < newInterval[start]:
        mergedIntervals.append(intervals[i])
        i += 1
    print(mergedIntervals)
    # merge the overlapping intervals
    while i < len(intervals) and intervals[i][start] <= newInterval[end]:
        newInterval[start] = min(intervals[i][start], newInterval[start])
        newInterval[end] = max(intervals[i][end], newInterval[end])
        i += 1

    # add the new interval
    mergedIntervals.append(newInterval)

    # merge the remaing intervals
    while i < len(intervals):
        mergedIntervals.append(intervals[i])
        i += 1
    return mergedIntervals


print(insertInterval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))

# Time O(n)
# space O(n)
