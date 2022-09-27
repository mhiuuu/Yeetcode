"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false"""

#Answer:
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n == 0):
            return False
        while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2
        return True
"""
Runtime: 22 ms
Memory Usage: 13.8 MB
Runtime beats 99.83 % of python3 submissions
Memory usage beats 95.72 % of python3 submissions
"""

"I found another solution which is much more easier than mine but it's not as efficient as mine. However it's pretty cool though"
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and n&(n-1)==0
"""
Runtime: 74 ms
Memory Usage: 13.8 MB
Runtime beats 8.97 % of python3 submissions
Memory usage beats 53.51 % of python3 submissions
"""

"""
Found this explanation on stackoverflow: "https://stackoverflow.com/questions/4678333/n-n-1-what-does-this-expression-do"
It's figuring out if n is either 0 or an exact power of two.

It works because a binary power of two is of the form 1000...000 and subtracting one will give you 111...111. Then, when you AND those together, you get zero, such as with:

  1000 0000 0000 0000
&  111 1111 1111 1111
  ==== ==== ==== ====
= 0000 0000 0000 0000
Any non-power-of-two input value (other than zero) will not give you zero when you perform that operation.

For example, let's try all the 4-bit combinations:

     <----- binary ---->
 n      n    n-1   n&(n-1)
--   ----   ----   -------
 0   0000   0111    0000 *
 1   0001   0000    0000 *
 2   0010   0001    0000 *
 3   0011   0010    0010
 4   0100   0011    0000 *
 5   0101   0100    0100
 6   0110   0101    0100
 7   0111   0110    0110
 8   1000   0111    0000 *
 9   1001   1000    1000
10   1010   1001    1000
11   1011   1010    1010
12   1100   1011    1000
13   1101   1100    1100
14   1110   1101    1100
15   1111   1110    1110
You can see that only 0 and the powers of two (1, 2, 4 and 8) result in a 0000/false bit pattern, all others are non-zero or true.
"""
