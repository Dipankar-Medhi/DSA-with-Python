
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


def rearrange(head):
    if head == None and head.next == None:
        return

    # find middle element
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # slow is at the middle
    head2 = reverse(slow)  # reverse the 2nd half
    head1 = head

    # rearrange
    while head1 and head2:
        temp1, temp2 = head1.next, head2.next
        head1.next = head2
        head2.next = temp1
        head1, head2 = temp1, temp2

    if head1:
        head1.next = None


def reverse(head):
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)
head.next.next.next.next.next = Node(12)

rearrange(head)
head.printLL()
