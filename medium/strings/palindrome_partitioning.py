"""Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters."""
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
            
        def part(f, st):
            if st == st[::-1]:
                res.append(f+[st])
            if len(st) == 1:
                return
                
            for i in range(1, len(st)):
                first = st[:i]
                if first == first[::-1]:
                    part(f + [first], st[i:])
                           
        part([], s)
        return res