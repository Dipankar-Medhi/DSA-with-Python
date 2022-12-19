import heapq


class Meeting:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end


def min_meeting_rooms(meetings):
    # sort the meetings by start time
    meetings.sort(key=lambda x: x.start)

    min_rooms = 0
    minHeap = []

    for meeting in meetings:
        # remove ended meetings
        while len(minHeap) > 0 and meeting.start >= minHeap[0].end:
            heapq.heappop(minHeap)

        # add current meeting into minHeap
        heapq.heappush(minHeap, meeting)

        # all active meetings are in min heap, so we need room for all of them
        min_rooms = max(min_rooms, len(minHeap))

    return min_rooms


print(min_meeting_rooms([Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)]))
