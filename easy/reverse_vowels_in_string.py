"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y"."""
class Solution:
    def reverseVowels(self, s: str) -> str:
        rev = []
        for i in range(len(s)):
            if s[i].lower() in ['a', 'e', 'i', 'o', 'u']:
                rev.append([i, s[i]])
        while len(rev) > 1:
            s = s[:rev[0][0]] + rev[-1][1] + s[rev[0][0]+1:]
            s = s[:rev[-1][0]] + rev[0][1] + s[rev[-1][0]+1:]
            rev = rev[1:-1]
        return s