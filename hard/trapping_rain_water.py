"""Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105"""

from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        water = [0]*len(height)
        stack = []
        for i, h in enumerate(height):
            if stack == []:
                stack.append([i,h])
            else:
                while len(stack) > 0 and stack[-1][1] < h:
                    a = stack.pop()
                if stack != []:
                    a = stack[-1]
                for idx in range(a[0]+1, i):
                    water[idx] = max(water[idx], min(a[1], h)-height[idx])
                stack.append([i,h])
                
        return sum(water)