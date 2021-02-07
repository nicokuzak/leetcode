"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        if (len(strs) == 0) or (min([len(x) for x in strs]) == 0):
            return ''
        while i < min([len(x) for x in strs]):
            if len(set([x[i] for x in strs])) > 1:
                break
            i += 1
        return strs[0][:i]