"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8"""

from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']
        res = set()
        cur = self.generateParenthesis(n-1)
        for pars in cur:
            for i in range(1, len(pars)+1):
                res.add(pars[:i]+ '()' + pars[i:])
        return list(res)