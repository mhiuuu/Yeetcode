/*
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
*/
//Answer:

/*
@param {number[]} nums
@return {boolean}
*/

var containsDuplicate = function(nums) {
    for(let i = 0; i < nums.length; i++) {
        for (let j = i+1; j < nums.length; j++) {
            if (nums[i] === nums[j]) {
                return true;
            }
        }
    }
    return false;
};


/*
Runtime: 848 ms
Memory Usage: 46.5 MB
Runtime beats 14.13 % of javascript submissions
Memory usage beats 96.20 % of javascript submissions
*/
