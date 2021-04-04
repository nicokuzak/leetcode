"""Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100"""
from typing import List
class Solution:
    #F'ed up X and Y, but works
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dx = dy = 1
        xr = [0, len(matrix)-1]
        yr = [0, len(matrix[0])-1]
        i = j = 0
        res = []
        cur = 'y'
        while len(res) < len(matrix)*len(matrix[0]):
            res.append(matrix[i][j])
            if cur == 'x':
                i += dx
                if i > xr[1]:
                    yr[1] -= 1
                    i -= 1
                    j += dy
                    dx *= -1
                    cur = 'y'
                    continue
                elif i < xr[0]:
                    yr[0] += 1
                    i += 1
                    j += dy
                    dx *= -1
                    cur = 'y'
                    continue

            if cur == 'y':
                j += dy
                if j > yr[1]:
                    xr[0] += 1
                    j -= 1
                    i += dx
                    dy *= -1
                    cur = 'x'
                    continue
                elif j < yr[0]:
                    xr[1] -= 1
                    j += 1
                    i += dx
                    dy *= -1
                    cur = 'x'
                    continue
        return res