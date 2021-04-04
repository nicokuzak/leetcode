"""Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6
 

Note:

S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50"""

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [S[0]]
        S = S[1:]
        while S != '':
            cur = S[0]
            if cur == ')':
                prev = stack.pop()
                if prev == '(':
                    stack.append(1)
                else:
                    while True:
                        nxt = stack.pop()
                        if nxt == '(':
                            break
                        prev += nxt
                    stack.append(prev*2)
            else:
                stack.append(cur)
            S = S[1:]
        if len(stack) > 1:
            return sum(stack)
        return stack[0]