"""Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
 

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'."""
class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '*':
                stack.append(c)
            elif c == ')':
                if stack == []:
                    return False
                last = stack.pop()
                new_stack = []
                while stack != [] and last == '*':
                    new_stack.append(last)
                    last = stack.pop()
                stack += new_stack    
        
        # Remaining stack should be of ( and *
        star = 0
        while stack != []:
            cur = stack.pop()
            if cur == '*':
                star += 1
            else:
                if star < 1:
                    return False
                star -= 1
        
        return True