import heapq


class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

    def __lt__(self, other):
        return self.val < other.val


def merge_lists(lists):
    minHeap = []

    # put root in the heap
    for root in lists:
        if root is not None:
            heapq.heappush(minHeap, root)

    # take the smallest(top) element and put inthe result and put the next element into the minheap
    resultHead, resultTail = None, None
    while minHeap:
        node = heapq.heappop(minHeap)
        # add to the root is empty
        if resultHead is None:
            resultHead = resultTail = node
        # keep appending
        else:
            resultTail.next = node
            resultTail = resultTail.next
        # add the next element of the node to the minHeap
        if node.next is not None:
            heapq.heappush(minHeap, node.next)

    return resultHead


l1 = ListNode(2)
l1.next = ListNode(6)
l1.next.next = ListNode(8)

l2 = ListNode(3)
l2.next = ListNode(6)
l2.next.next = ListNode(7)

result = merge_lists([l1, l2])
while result is not None:
    print(result.val)
    result = result.next
