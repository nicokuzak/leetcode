"""Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

    Returns:
        [type]: [description]
    """

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        ret = []
        count = 0
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            val = -nums[i]
            if val < 0:
                break
            while j < k:
                count += 1
                if j > i + 1 and nums[j] == nums[j-1]:
                    j += 1
                    continue
                if k < len(nums) - 1 and nums[k] == nums[k + 1]:
                    k -= 1
                    continue
                if nums[j] > val:
                    break
                curr = nums[j] + nums[k]
                if curr == val:
                    ret.append([nums[i], nums[j], nums[k]])
                    k -= 1
                elif curr < val:
                    j += 1
                else:
                    k -= 1
        return ret