"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""
#Answer:
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = [number ** 2 for number in nums]
        return sorted(arr)

"""
Runtime 507 ms Beats 40.93%
Memory 16.4 MB Beats 18%
"""
