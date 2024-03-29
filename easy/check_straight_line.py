"""You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 

 

Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point."""
from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 3:
            return True
        slope = self.get_slope(coordinates[0], coordinates[1])
        for i in range(2, len(coordinates)):
            if self.get_slope(coordinates[i], coordinates[i-1]) != slope:
                return False
        return True
    
    def get_slope(self, one, two):
        y = two[1] - one[1]
        x = two[0] - one[0]
        if x == 0:
            return float('inf')
        return y/x