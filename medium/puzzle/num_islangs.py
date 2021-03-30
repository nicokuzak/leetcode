"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'."""
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(i,j, grid)
        return res

    def dfs(self, i, j, grid):
        if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[i])-1 or grid[i][j]=='0':
            return 0
        grid[i][j] = '0'
        self.dfs(i - 1, j, grid)
        self.dfs(i + 1, j, grid)
        self.dfs(i, j + 1, grid)
        self.dfs(i, j - 1, grid)