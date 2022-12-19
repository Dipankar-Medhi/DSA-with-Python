class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


def find_middle_of_linked_list(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.val


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print(find_middle_of_linked_list(head))
