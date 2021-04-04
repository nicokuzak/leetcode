"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
"""
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        self.res = False
        def dfs(board, word, i, j, used):
            if self.res:
                return
            if board[i][j] == word[0]:
                if len(word) == 1:
                    self.res = True
                word = word[1:]
                used.append([i,j])
            else:
                return
            if i + 1 < m and [i+1,j] not in used:
                dfs(board, word, i+1, j, used[:])
            if i-1 > -1 and [i-1, j] not in used:
                dfs(board, word, i-1, j, used[:])
            if j+1 < n and [i, j+1] not in used:
                dfs(board, word, i, j+1, used[:])
            if j-1 > -1 and [i, j-1] not in used:
                dfs(board, word, i, j-1, used[:])
                
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    dfs(board, word, i, j, [])
                if self.res:
                    break
            if self.res:
                break
        return self.res