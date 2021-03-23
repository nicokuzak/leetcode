"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        pointers = [0]*numRows
        i = 0
        p = 1
        adding = True
        ret = ''
        while i < len(s):
            ret = ret[:pointers[p-1]] + s[i] + ret[pointers[p-1]:]
            for j, val in enumerate(pointers):
                if j >= p - 1:
                    pointers[j] = val + 1
            if numRows == 1:
                p = 1
            elif p == numRows:
                p -= 1
                adding = False
            elif p == 1:
                p += 1
                adding = True
            elif adding:
                p += 1
            else:
                p -= 1
            i += 1
        return ret
            
            
            