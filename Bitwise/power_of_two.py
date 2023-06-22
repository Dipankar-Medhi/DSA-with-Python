""" 
Given an integer n, write a function to determine if it is a power of two.

Example 1:
Input: n = 1
Output: true 
Explanation: 2^0 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 2^4 = 16
"""

def isPowerOfTwo(n): 
    # counting the number of set bits 

    # if n % 2 then n = 10000...
    # and n - 1 is 01111..
    # so, n & (n - 1) is 000000..
    return n > 0 and (n & (n - 1)) == 0

print(isPowerOfTwo(8))
