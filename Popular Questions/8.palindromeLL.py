"""
Given a LL of integers list, create a boolean function that checks if it's a palindrome linked list in constant space complexity.
"""

# Steps:
# 1. find the beginning of right half
# 2. reverse the right half
# 3. compare the two halves

# Slow and fast pointer method

# ---------------------------------- #
# when fast at null , slow at mid
# ----------------------------------- #

# TIme O(n) & Space O(1)


def reverseList(head):
    previous = None
    current = head
    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous


def isPalindrome(list):
    slow = fast = list.head
    # while fast and fast.next is not none
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # slow will be at the mid, so we reverse the right half
    slow = reverseList(slow)
    head = list.head
    # while slow is not None
    while slow:
        # check if data is equal
        if slow.data != head.data:
            return False
        slow = slow.next
        head = head.next
    return True
