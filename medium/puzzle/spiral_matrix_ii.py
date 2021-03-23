"""Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
"""

from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for i in range(n)]
        num = 0
        i = 0
        j = -1
        
        dx = -1
        dy = -1
        
        move_amt = n
        
        while num < n*n:
            count += 1
            dx *= -1
            dy *= -1
            
            for _ in range(move_amt):
                num += 1
                j += dx
                matrix[i][j] = num
                
            move_amt -= 1
            
            for _ in range(move_amt):
                num += 1
                i += dy
                matrix[i][j] = num
        return matrix