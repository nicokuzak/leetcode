"""Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
 

Constraints:

n == nums.length
1 <= n <= 104
-105 <= nums[i] <= 105
"""

from typing import List
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        num = 0
        if len(nums) < 3:
            return True
        max_num = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                num += 1
                if nums[i+1] < max_num:
                    nums[i+1] = nums[i]
                else:
                    nums[i] = nums[i+1]
            max_num = max(max_num, nums[i])
            if num > 1:
                return False
        return True