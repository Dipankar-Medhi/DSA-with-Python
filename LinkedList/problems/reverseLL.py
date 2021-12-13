# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        prev = None
        pres = head
        nextnode = pres.next

        while pres != None:
            pres.next = prev
            prev = pres
            pres = nextnode
            if nextnode != None:
                nextnode = nextnode.next

        return prev
