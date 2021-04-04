"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'."""

from typing import List
class Solution:
    import math
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        m = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                    m = max(m, int(matrix[i][j]))
                elif matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    up, left, diag = dp[i-1][j], dp[i][j-1], dp[i-1][j-1]
                    if up > 0 and left > 0 and diag > 0:
                        n = int(math.sqrt(min(up, left, diag))+1)**2
                        dp[i][j] = n
                        m = max(m, n)
                    else:
                        dp[i][j] = 1
                        m = max(m, 1)
        return m