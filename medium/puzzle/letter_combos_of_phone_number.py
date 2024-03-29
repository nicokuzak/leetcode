    """Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
    """

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
             '6':'mno',
             '7':'pqrs',
             '8':'tuv',
             '9':'wxyz'
            }
        if digits == '':
            return []
        lists = []
        for x in digits:
            lists.append([char for char in d[x]])
        ret = lists[0]
        lists = lists[1:]
        while len(lists) > 0:
            ret = self.combo(ret, lists[0])
            lists = lists[1:]
        return ret
            
    
    def combo(self, l, s):
        if s == []:
            return s
        return [x+s[0] for x in l] + self.combo(l, s[1:])