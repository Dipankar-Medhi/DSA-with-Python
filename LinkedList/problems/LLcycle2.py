# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        f, s = head, head
        if not s:
            return None

        if not s.next:
            return None
        while f and f.next:
            f = f.next.next
            s = s.next
            if f == s:
                break
        if f == s:
            while f != head:
                f = f.next
                head = head.next

            return head
        return None
