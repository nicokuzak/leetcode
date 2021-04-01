"""Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500]."""

from collections import Counter
import math
class Solution:
    def reorganizeString(self, S: str) -> str:
        c = Counter(S)
        if max([v for k,v in c.items()]) > math.ceil(len(S)/2):
            return ''
        res = ''
        while len(res) < len(S):
            if len(c) == 1:
                res += [k for k in c.keys()][0]
                break
            else:
                mc = c.most_common()
                most = mc[0]
                least = mc[-1]
            res += most[0] + least[0]
            c[most[0]] -= 1
            if c[most[0]] == 0:
                del(c[most[0]])
            c[least[0]] -= 1
            if c[least[0]] == 0:
                del(c[least[0]])
        return res      