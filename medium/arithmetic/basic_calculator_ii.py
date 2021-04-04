
"""Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer."""
class Solution:
    import re
    def calculate(self, s: str) -> int:
        def add(one, two):
            return one + two
        def multiply(one, two):
            return one*two
        def subtract(one, two):
            return one-two
        def divide(one, two):
            return one//two
        
        def get_digit(s):
            cur = ''
            while s != '' and s[0].isdigit():
                cur += s[0]
                s = s[1:]
            return int(cur), s
        # Make a stack to multiply/divide, then change to a queue to add
        stack = []
        s = re.sub(' +', '', s)
        while s != '':
            # Get current number, can be > 9
            if s[0].isdigit():
                cur, s = get_digit(s)
                stack.append(int(cur))
            elif s[0] == '*':
                num_to_multiply, s = get_digit(s[1:]) 
                prev = stack.pop()
                stack.append(multiply(prev, num_to_multiply))
            elif s[0] == '/':
                num_to_multiply, s = get_digit(s[1:]) 
                prev = stack.pop()
                stack.append(divide(prev, num_to_multiply))
            else:
                stack.append(s[0])
                s = s[1:]
        
        # Now need to add and divide, queue.pop(0)
        res = stack.pop(0)
        while stack != []:
            cur = stack.pop(0)
            if cur == '-':
                res = subtract(res, stack.pop(0))
            elif cur == '+':
                res = add(res, stack.pop(0))
            else:
                print('Something went wrong')
        return res