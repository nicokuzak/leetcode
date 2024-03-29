"""Given an integer n, return a list of all simplified fractions between 0 and 1 (exclusive) such that the denominator is less-than-or-equal-to n. The fractions can be in any order.

 

Example 1:

Input: n = 2
Output: ["1/2"]
Explanation: "1/2" is the only unique fraction with a denominator less-than-or-equal-to 2.
Example 2:

Input: n = 3
Output: ["1/2","1/3","2/3"]
Example 3:

Input: n = 4
Output: ["1/2","1/3","1/4","2/3","3/4"]
Explanation: "2/4" is not a simplified fraction because it can be simplified to "1/2".
Example 4:

Input: n = 1
Output: []
 

Constraints:

1 <= n <= 100"""

from typing import List
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        def fracs(n):
            for j in range(1, n):
                if j == 1:
                    res.append(str(j)+'/' + str(n))
                elif self.lcd(j, n):
                    res.append(str(j)+'/' + str(n))
        for i in range(2, n+1):
            fracs(i)
        return res
    
    def lcd(self, a, b):
        for i in range(2, a+1):
            if float(a//i) == a/i:
                if float(b//i) == b/i:
                    return False
        return True