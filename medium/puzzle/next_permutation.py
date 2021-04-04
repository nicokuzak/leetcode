"""Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        queue = []
        j = len(nums) - 1
        while j > 0:
            queue.append([nums[j], j])
            if nums[j-1] < nums[j]:
                val, idx = queue.pop(0)
                while queue != [] and val <= nums[j-1]:
                    val, idx = queue.pop(0)
                nums[j-1], nums[idx] = nums[idx], nums[j-1]
                nums[j:] = sorted(nums[j:])
                break
            j -= 1
        
        if j == 0:
            nums[:] = sorted(nums)