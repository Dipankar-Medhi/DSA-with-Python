class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # fast and slow at the head
        fast = head
        slow = head

        # fast move by 2 position and slow by 1 ----- this is Fast and Slow pointer method
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
        
        # if fast or fast.next is null i.e the list is not a cycle, return false
        return False

    ## find the length of the cycle
    def lengthOfCycle(self, head: ListNode):
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                temp = slow
                len = 0
                while temp.next != slow:
                    len +1
                    temp = temp.next
                return len

        return 0