"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
"""
#Answer:
class Solution:
    def reverseWords(self, s: str) -> str:
        str1 = ""
        arr = [list(x) for x in s.split()]
        for i in range(len(arr)):
            arr[i].reverse()
            arr[i].append(" ")
        flatten_list = [j for sub in arr for j in sub]
        flatten_list.pop()
        return str1.join(flatten_list) 
       
"""
Runtime 46 ms Beats 86.54%
Memory 15.3 MB Beats 12.93%
"""
