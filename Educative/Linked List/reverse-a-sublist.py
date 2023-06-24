"""
- Skip the first p-1 nodes, to reach the node at position p.
- Remember the node at position p-1 to be used later to connect with the reversed sub-list.
- Next, reverse the nodes from p to q using the same approach discussed in Reverse a LinkedList.
- Connect the p-1 and q+1 nodes to the reversed sub-list.
"""


class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

    def printLL(self):
        temp = self
        while temp:
            print(str(temp.value) + " ", end="")
            temp = temp.next
        print()


def reverseSublist(head, p, q):
    if p == q:
        return head

    # current node will be p after skipping p - 1 nodes
    curr, prev = head, None

    i = 0
    while curr and i < p - 1:
        prev = curr
        curr = curr.next
        i += 1

        print(f"prev: {prev.value}, curr: {curr.value}")
    # there are 3 parts, 1 till p-1, 2nd between p and q, and 3rd after q
    last_node_of_first_part = prev
    # after reversing the LinkedList 'current' will become the last node of the sub-list
    last_node_of_sub_list = curr

    next = None
    i = 0
    # reverse nodes between 'p' and 'q'
    while curr is not None and i < q - p + 1:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        i += 1
    print(f"prev2: {prev.value}, curr2: {curr.value}")
    # connect with the first part
    if last_node_of_first_part is not None:
        # 'prev' is now the first node of the sub-list
        last_node_of_first_part.next = prev
    # this means p == 1 i.e., we are changing the first node (head) of the LinkedList
    else:
        head = prev

    # connect with the last part
    last_node_of_sub_list.next = curr
    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
result = reverseSublist(head, 2, 4)
result.printLL()
