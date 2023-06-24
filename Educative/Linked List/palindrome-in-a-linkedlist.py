class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


def isPalindrome(head):
    if head is None or head.next is None:
        return True

    # find the middle element
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the 2nd half
    head2 = reverse(slow)

    # compare 1st and 2nd half elements
    while head and head2:
        if head.value != head2.value:
            break
            # or return False

        head = head.next
        head2 = head2.next
    # if all the elements are similar, the head will reach the end i.e None

    if head is None or head2 is None:
        return True

    return False


def reverse(head):
    prev = None

    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev


head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(1)


print(isPalindrome(head))
