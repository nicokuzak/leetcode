"""Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = False
        for x in range(len(matrix)):
            if matrix[x][-1] >= target:
                row = matrix[x]
                break
        if not row:
            return False
        if len(row) == 1:
            if row[0] == target:
                return True
            return False
        i = 0
        j = len(row)-1
        while i <= j:
            mid = (i+j)//2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return False