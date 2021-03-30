"""Given an unsorted integer array nums, find the smallest missing positive integer.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
 

Constraints:

0 <= nums.length <= 300
-231 <= nums[i] <= 231 - 1"""

from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        pos = [0]*(len(nums)+1)
        for num in nums:
            if num > len(nums):
                continue
            if num > 0:
                pos[num-1] = 1
        for i, j in enumerate(pos):
            if j == 0:
                return i+1
        return len(pos) +1