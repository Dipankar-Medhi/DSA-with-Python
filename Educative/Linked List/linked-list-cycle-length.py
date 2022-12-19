
class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


def findCycleLength(head):
    slow, fast = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:  # has a cycle
            return cycleLength(slow)

    return False


def cycleLength(slow):
    current = slow
    cycle_len = 0

    while True:
        current = current.next
        cycle_len += 1

        if current == slow:
            break
    return cycle_len


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = head.next.next

print(findCycleLength(head))
