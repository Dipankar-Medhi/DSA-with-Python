"""
Given an array of integers arr that contains n+1 elements between 1 and n inclusive, create a function that returns the dupicate element (element that appears more than once)

Assume:
1. There is only one duplicate number
2. Duplicate number can be repeated more than once
"""
# -------------------------- #
# Pigeonhole principle :
# if we try to insert n items in m containers and n > m,
# then at least two items will share same containers

# --------------------------- #

# Brute force soln ---> time O(n2)
# for earch element, we search for it in the remaing elements,
# if we find it, then its the duplicate


def findDuplicate(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]

##############################################
# sorting soln like we did in Q2

##############################################

# Hash table ---> time O(n)

##############################################
# ------------------------------------------ #
# Floyd's cycle detection algorithm (tortoise and hare)/(fast and slow)
# pointer technique ---> can use in linked list to check cycle

# slow move by 1, fast move by 2.
# keep moving until they meet, if they do meet, mean theres a cycle.
# to find the point of cycle, once the pointers meet,
# we put slow at the beginning and move fast by 1.
# The point at which they meet is the point of start of cycle.

# ------------------------------------------# arr = [5, 2, 4, 3, 1, 2]
# time O(n) space O(1)


def findDuplicate2(arr):
    # 1 unit distance -> 1st element
    slow = arr[0]
    # 2 unit distance
    fast = arr[arr[0]]

    # while they donot meet
    while slow != fast:
        # keep moving them
        slow = arr[slow]
        fast = arr[arr[fast]]
    # once met, move slow to begining
    slow = 0
    # move both fast and slow by 1 unit
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    # point where they meet is answer
    return slow


print(findDuplicate2([5, 2, 4, 3, 1, 2]))


############################################
