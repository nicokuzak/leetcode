"""Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 3 * 104
0 <= nums[i] <= 105"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                break
            if max_reach >= len(nums) - 1:
                return True
            max_reach = max(max_reach, nums[i]+i)
        if max_reach >= len(nums) - 1:
            return True
        return False