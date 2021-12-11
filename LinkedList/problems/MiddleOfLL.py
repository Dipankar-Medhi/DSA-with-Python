# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        f = head
        s = head

        while f != None and f.next != None:
            s = s.next
            f = f.next.next

        return s
