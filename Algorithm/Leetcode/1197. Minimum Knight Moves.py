class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        knight_move = [[1,2], [2,1], [2,-1], [1,-2], [-2,1], [-1,2]]
        k_x, k_y = 0, 0
        ans = 0
        
        q = deque([(0,0,0)])
        k_x, k_y, visit = abs(x), abs(y), set([0,0])
        
        while q:
            k_x, k_y, step = q.popleft()
            if (k_x, k_y) == (x, y): 
                return step
            for i in range(len(knight_move)):
                if (k_x + knight_move[i][0], k_y + knight_move[i][1]) not in visit and -1 <=k_x + knight_move[i][0] <= x+2 and -1<= k_y + knight_move[i][1] <= y+2:
                    visit.add((k_x + knight_move[i][0], k_y + knight_move[i][1]))
                    q.append((k_x + knight_move[i][0], k_y + knight_move[i][1], step+1))
                
        return -1