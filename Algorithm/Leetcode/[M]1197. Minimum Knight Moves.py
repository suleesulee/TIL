class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        knight_move = [[1, 2], [2, 1], [2, -1], [1, -2], [-2, 1], [-1, 2], [-1, -2],[-2, -1]]
        k_x, k_y = 0, 0
        ans = 0
        
        q = deque([(0,0,0)])
        k_x, k_y, visit = 0, 0, set([0,0])
        
        while q:
            k_x, k_y, step = q.popleft()
            if (k_x, k_y) == (x, y): 
                return step
            
            for i in range(len(knight_move)):
                next_x = k_x + knight_move[i][0]
                next_y = k_y + knight_move[i][1]
                
                if (next_x, next_y) not in visit:
                    visit.add((next_x, next_y))
                    q.append((next_x, next_y, step + 1))
                
        return -1
    

# BFS문제 생각보다 오랜시간이 소요된다...