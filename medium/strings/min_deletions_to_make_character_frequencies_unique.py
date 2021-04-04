"""A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

 

Example 1:

Input: s = "aab"
Output: 0
Explanation: s is already good.
Example 2:

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
Example 3:

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
 

Constraints:

1 <= s.length <= 105
s contains only lowercase English letters."""

from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        vals = [v for k, v in c.items()]
        num_c = Counter(vals)
        res = 0
        max_ = max(num_c.keys())
        for i in range(max_):
            if i not in num_c.keys():
                num_c[i] = 0
        for k, v in num_c.items():
            if v < 2:
                continue
            key, val = k, v
            while val > 1:
                while num_c[key] > 0:
                    key -= 1
                    res += 1
                num_c[k] -= 1
                val -= 1
                if key != 0:
                    num_c[key] = 1
                key = k
        return res
        
                
            
                    
                
        
        