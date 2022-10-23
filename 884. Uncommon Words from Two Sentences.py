"""
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]
"""
#Answer:
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        arr1 = s1.split(" ") + s2.split(" ")
        arr = [i for i in arr1 if arr1.count(i) == 1]
        return arr
      
"""
Runtime 35 ms Beats 90.32% 
Memory 13.8 MB Beats 68.83%
"""
