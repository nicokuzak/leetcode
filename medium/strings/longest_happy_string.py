"""A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.

Given three integers a, b and c, return any string s, which satisfies following conditions:

s is happy and longest possible.
s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.
s will only contain 'a', 'b' and 'c' letters.
If there is no such string s return the empty string "".

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 2, b = 2, c = 1
Output: "aabbc"
Example 3:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It's the only correct answer in this case.
 

Constraints:

0 <= a, b, c <= 100
a + b + c > 0"""
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        self.list = [[a,'a'], [b,'b'], [c,'c']]
        def create_string(s):
            self.list.sort()
            if self.list[2][0] == 0:
                return s
            i = 2
            if len(s) > 1 and s[-2] == self.list[2][1] and s[-1] == self.list[2][1]:
                i = 1
                if self.list[1][0] == 0:
                    return s
            s += self.list[i][1]
            self.list[i][0] = self.list[i][0] - 1
            return create_string(s)
        return create_string('')