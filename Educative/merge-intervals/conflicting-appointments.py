def can_attend_all_appointments(intervals):
    intervals.sort(key=lambda x: x[0])
    start, end = 0, 1

    for i in range(1, len(intervals)):
        # we just need to check if they are overlapping
        if intervals[i][start] < intervals[i - 1][end]:
            return False

    return True


print(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]]))
