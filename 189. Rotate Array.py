"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""
#Answer:
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            check = nums.pop()
            nums.insert(0, check)
            
"""
Time complexity O(n) depends on k
Space complexity O(1) don't need to create any extra memories
Runtime 3381 ms Beats 5%
Memory 25.4 MB Beats 76.19%
"""
