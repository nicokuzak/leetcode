"""Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

 

Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]
 

Note:

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9"""
from typing import List
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        if len(A) == 0:
            return []
        A.sort()
        ret = [0]*len(A)
        i = 0
        B = [x for x in enumerate(B)]
        B = sorted(B, key = lambda x: x[1])
        while A != []:
            if A[0] <= B[0][1]:
                ret[B[-1][0]] = A[i]
                A = A[1:]
                B = B[:-1]
            else:
                ret[B[0][0]] = A[0]
                A = A[1:]
                B = B[1:]
        return ret