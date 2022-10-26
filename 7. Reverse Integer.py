"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
"""
#Answer:
class Solution:
    def reverse(self, x: int) -> int:
        #Check here is used to make sure that if x is negative so in the end we can add the "-" becuz we can't convert int into list if x is negative
        check = False
        if x < 0:
            check = True
            #x is now converted positive number
            x = abs(x) 
        arr = [int(i) for i in str(x)]
        n = int("".join(map(str, arr[::-1])))
        if check:
            #So if x < 0 check will be true so we can add "-"
            n = -n 
        #Control overflow
        if -n not in range(-2**31, 2**31-1) or n not in range(-2**31, 2**31-1):
            return 0
        return n
"""
Time complexity O(n): we convert int into arr with list comprehesion
Space complexity O(n): need extra memory for the arr
Runtime 58 ms Beats 58.24%
Memory 13.8 MB Beats 64.49%
"""
