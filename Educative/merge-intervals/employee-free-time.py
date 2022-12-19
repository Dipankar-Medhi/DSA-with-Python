from __future__ import print_function
from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end="")


class EmployeeInterval:
    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval  # interval representing employee's working hours
        # index of the list containing working hours of this employee
        self.employeeIndex = employeeIndex
        self.intervalIndex = intervalIndex  # index of the interval in the employee list

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.interval.start < other.interval.start


def find_employee_free_time(schedule):
    if schedule is None:
        return []

    n = len(schedule)
    result, minHeap = [], []

    # insert first interval of each employee
    for i in range(n):
        heappush(minHeap, EmployeeInterval(schedule[i][0], i, 0))

    prevInterval = minHeap[0].interval

    while minHeap:
        top = heappop(minHeap)

        if prevInterval.end < top.interval.start:
            result.append(Interval(prevInterval.end, top.interval.start))
            prevInterval = top.interval
        else:
            if prevInterval.end < top.interval.end:
                prevInterval = top.interval

        employeeSchedule = schedule[top.employeeIndex]
        if len(employeeSchedule) > top.intervalIndex + 1:
            heappush(minHeap, EmployeeInterval(employeeSchedule[top.intervalIndex]))
