"""Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        lst = [int(x) for x in list(str(num))]
        i = 0   
        while i < len(lst) - 1:
            mx = max(lst[i+1:])
            if lst[i] < mx:
                idx = i
                for j in reversed(range(i+1, len(lst))):
                    if lst[j] == mx:
                        idx = j
                        break
                lst[i], lst[idx] = lst[idx], lst[i]
                break
            i += 1
        return int(''.join([str(x) for x in lst]))