"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""
#Answer:
class Solution(object):
    def lengthOfLastWord(self, s):
        if s.split():
            return len(s.split()[-1])
        return 0
      
"""
Time complexity O(n): for the split()
Space complexity O(n): space for the s.split()
Runtime 60 ms Beats 30.91%
Memory 13.9 MB Beats 80.1%
"""
