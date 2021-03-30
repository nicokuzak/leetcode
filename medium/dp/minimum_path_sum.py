"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100"""
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 1:
            return sum(grid[0])
        dp = [[0]*len(grid[0]) for x in range(len(grid))]
        for i in range(0, len(grid)):
            for j in range(len(grid[0])):
                if i == 0:
                    if j == 0:
                        dp[i][j] = grid[i][j]
                    else:
                        dp[i][j] = dp[i][j-1] + grid[i][j]
                else:
                    if j == 0:
                        dp[i][j] = dp[i-1][j]+grid[i][j]
                    else:
                        dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1]+grid[i][j])
        return dp[len(grid)-1][len(grid[0])-1]

# BFS - Time Limit Exceeded
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         if len(grid) == 1:
#             return sum(grid[0])
#         m = float('inf')
#         i = len(grid)-1
#         j = len(grid[0])-1
#         stack = [[i,j,0]]
#         while stack != []:
#             cur = stack.pop()
#             i, j = cur[0], cur[1]
#             if i == 0 and j == 0:
#                 m = min(m, cur[2]+grid[i][j])
#                 continue
#             score = cur[2]+grid[i][j]
#             if score > m:
#                 continue
#             if i - 1 > -1:
#                 stack.append([i -1, j, score])
#             if j-1 > -1:
#                 stack.append([i, j-1, score])
#         return m