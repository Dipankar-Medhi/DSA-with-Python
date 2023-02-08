import heapq

""" 
Max heap -> store the smaller half
Min heap -> store the larger half
"""


class MedianOfAStream:
    maxHeap = []  # 1st half
    minHeap = []  # 2nd half

    def insertNum(self, num):
        # num > max of maxhead goes to minheap, num < max of maxheap goes to maxheap
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        # both heap should contain equal number of elements or max heap should have one more elements than minheap.

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        print("Minheap and Maxheap:", self.minHeap, self.maxHeap)

    def findMedian(self):
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        return -self.maxHeap[0]


def main():
    medianofastream = MedianOfAStream()
    medianofastream.insertNum(3)
    medianofastream.insertNum(1)
    print("Median is : " + str(medianofastream.findMedian()))
    medianofastream.insertNum(5)
    print("Median is : " + str(medianofastream.findMedian()))

    medianofastream.insertNum(4)
    print("Median is :" + str(medianofastream.findMedian()))


main()
