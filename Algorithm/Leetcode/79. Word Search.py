class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m, self.n = len(board), len(board[0])
        self.board = board
        
        for x in range(self.m):
            for y in range(self.n):
                if board[x][y] == word[0]:
                    if self.backtrack(x, y, word):
                        return True
                
        return False
        
        
    def backtrack(self, m, n, suffix):
        if len(suffix) == 0:
            return True
        
        if m < 0 or m == self.m or n < 0 or n == self.n or self.board[m][n] != suffix[0]:
            return False
        
        ret = False
        
        self.board[m][n] = '#'
        
        for i, j in [(1,0), (0,1), (-1,0), (0,-1)]:
            ret = self.backtrack(m + i, n + j, suffix[1:])
            if ret:
                break
                
        self.board[m][n] = suffix[0]
        
        return ret
                                
        79. Word Search
