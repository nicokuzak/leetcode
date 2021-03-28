"""Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100]."""
from typing import List
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        dp = [0]*len(T)
        i = len(T)-2
        stack = [[len(T)-1, T[-1]]]
        
        while i >-1:
            while len(stack) > 0 and stack[-1][1] <= T[i]:
                stack.pop()
            if stack != []:
                dp[i] = stack[-1][0] - i
            stack.append([i, T[i]])
            i -= 1
        return dp