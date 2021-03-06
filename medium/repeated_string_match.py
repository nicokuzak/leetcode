""" 
Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.

Notice: string "abc" repeated 0 times is "",  repeated 1 time is "abc" and repeated 2 times is "abcabc".

 

Example 1:

Input: a = "abcd", b = "cdabcdab"
Output: 3
Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.
Example 2:

Input: a = "a", b = "aa"
Output: 2
Example 3:

Input: a = "a", b = "a"
Output: 1
Example 4:

Input: a = "abc", b = "wxyz"
Output: -1
 

Constraints:

1 <= a.length <= 104
1 <= b.length <= 104
a and b consist of lower-case English letters.
"""

class Solution:
    import math
    def repeatedStringMatch(self, a: str, b: str) -> int:
        i = 1
        orig_a = a
        if a == '':
            return -1
        if b in a:
            return 1
        else:
            while len(a) <= len(b):
                i += 1
                a = orig_a*i
            if b in a[:len(a)-len(orig_a)]:
                return i-1
            if b in a:
                return i
            if b in a + orig_a:
                return i +1
        return -1