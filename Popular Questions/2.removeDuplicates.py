"""
Given an array of integers arr, create a function that returns an array that contains the values of arr without duplicates (the order doesn't matter)
"""
# time O(n2) & space O(n)
from sympy import real_root


def removeDuplicates(arr):
    # arr to store the non duplicate elements
    noDup = []
    # for each element,
    for ele in arr:
        # if the element is not in no duplicate arr, we store that element in the no dup arr
        if ele not in noDup:
            noDup.append(ele)
    # at last we return the no dup arr
    return noDup

# -------------------------#

# sorting the array -> then skip the duplicate elements ---- time O(nlogn) & space O(n)


def removeDuplicates2(arr):
    # null arr ---> return []
    if len(arr) == 0:
        return []
    # sorting the arr 1st
    arr.sort()
    # new arr to store the elements --> start by 1st element
    noDup = [arr[0]]
    # check if current is equal to previous, if no then we add to new arr, else we skip
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            noDup.append(arr[i])
    return noDup


# Hash table --- time O(n) & space O(n)
# for each element we add element: true in the hash table, then we take the keys and turn it into array

def removeDuplicates3(arr):
    # hash table to store the elements
    visited = {}
    # for each element we add element : true in hash table
    for element in arr:
        visited[element] = True
    # finally we return the keys converted to list
    return list(visited.keys())


print(removeDuplicates3([4, 2, 3, 2, 4, 1]))
