class Interval:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def printInterval(self):
        print("[" + str(self.start) + "," + str(self.end) + "]", end="")


def mergeIntervals(intervals):
    # return interval if there is less than 2
    if len(intervals) < 2:
        return intervals

    # sort the intervals based on the start value
    intervals.sort(key=lambda x: x.start)

    # store merged intervals
    mergeIntervalsArr = []
    # take 1st interval for comparison
    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]
        # adjust end for overlapping intervals
        if interval.start <= end:
            end = max(end, interval.end)
        # add previous interval and move the stat and end
        else:
            mergeIntervalsArr.append(Interval(start, end))
            start = interval.start
            end = interval.end

        # add the last interval to the arr
    mergeIntervalsArr.append(Interval(start, end))
    return mergeIntervalsArr


def main():
    for i in mergeIntervals([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.printInterval()

    print()


main()
