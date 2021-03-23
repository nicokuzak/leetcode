""" 
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 104
-109 <= nums[i] <= 109
"""
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        nums.sort()
        cur = 1
        longest = cur
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                cur += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                if cur > longest:
                    longest = cur
                cur = 1
        if cur > longest:
            longest = cur
        return longest