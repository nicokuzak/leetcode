"""Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105"""
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #sliding window
        i = j = 0
        res = []
        while i < len(nums):
            while j < len(nums):
                j += 1
                if sum(nums[i:j]) >= target:
                    if j-i < len(res) or res == []:
                        res = nums[i:j]
                    break
            
            if j >= len(nums)-1 and sum(nums[i:j]) < target:
                break
                
            while i < j:
                i += 1
                if sum(nums[i:j]) >= target:
                    if j-i < len(res):
                        res = nums[i:j]
                else:
                    break
        return len(res)