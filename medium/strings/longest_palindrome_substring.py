""" 
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        len_longest = 0
        for i in range(len(s)):
            j = len(s)
            while i < j and j - i > len_longest:
                current = s[i:j]
                if current == current[::-1]:
                    longest = current
                    len_longest = len(current)
                    break
                j -= 1
        return longest