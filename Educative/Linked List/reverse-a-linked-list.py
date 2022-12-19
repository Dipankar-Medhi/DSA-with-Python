class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next
        print()


def reverse(head):
    prev, curr, next = None, head, None

    while curr is not None:
        next = curr.next  # temporarily store the next node
        curr.next = prev  # reverse the curr node
        prev = curr  # point prev to curr
        curr = next  # move to next node

    return prev


head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)

print("Nodes of original LinkedList are: ", end="")
head.print_list()
result = reverse(head)
print("Nodes of reversed LinkedList are: ", end="")
result.print_list()
