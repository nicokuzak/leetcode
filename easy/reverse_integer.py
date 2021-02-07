"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1
"""
import math

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        neg = 1
        if x < 0:
            neg = -1
            x = x*neg
        lst = []
        while x != 0:
            lst.append(x % 10)
            x = math.floor(x/10)
        print(lst)
        ret = 0
        for i in range(len(lst)):
            ret += lst[i]*10**(len(lst)-i-1)
        if (ret < -2**31) or (ret > 2**31 - 1):
            return 0
        return ret*neg