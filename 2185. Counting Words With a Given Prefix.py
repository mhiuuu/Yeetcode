"""
You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.

 

Example 1:

Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
Example 2:

Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.
"""
#Answer:
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        words_splited = []
        for i in words:
            words_splited.append([x for x in i])
        arr = [x for x in pref]
        count = 0
        for i in words_splited:
            if i[:len(arr)] == arr:
                count += 1
        return count
      
"""
Runtime 65 ms Beats 69.64%
Memory 14 MB Beats 26.71%
"""
