# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find the middle element
        s, f = ListNode(None, head), head
        while f and f.next:
            s = s.next
            f = f.next.next
        start, mid, s.next = head, s.next, None

        # 2. reverse second half
        prev = None
        while mid:
            mid.next, prev, mid, = prev, mid, mid.next
        mid = prev

        # 3. compare
        while start and mid:
            if start.val != mid.val:
                return False
            start, mid = start.next, mid.next
        return True

