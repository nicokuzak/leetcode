"""
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Example 2:

Input: s = "a", t = "a"
Output: "a"
 

Constraints:

1 <= s.length, t.length <= 105
s and t consist of English letters.
 

Follow up: Could you find an algorithm that runs in O(n) time?"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t =='':
            return ''
        ct = Counter(t)
        cs = {k:0 for k in ct.keys()}
        m = ''
        min_len = float('inf')
        i = 0
        j = -1
        while i < len(s):
            if j == len(s)-1:
                break
            while j < len(s)-1:
                j += 1
                if s[j] in t:
                    cs[s[j]] =  cs[s[j]] + 1
                    if self.isValid(cs, ct):
                        if j+1-i < min_len:
                            min_len = j+1-i
                            m = s[i:j+1]
                        break
                
            while i < j:
                i+= 1
                if s[i-1] in cs.keys():
                    cs[s[i-1]] = cs[s[i-1]] - 1
                if self.isValid(cs, ct):
                    if j-i < min_len:
                        min_len = j-i
                        m = s[i:j+1]
                else:
                    break
        return m
                        
                    
    def isValid(self, cs, ct):
        for k in ct.keys():
            if cs[k] < ct[k]:
                return False
        return True