'''
완전탐색문제
BFS, DFS 둘다 풀어낼수있다.
파이썬의 간단함과 deque의 사용법을 잘 알아야한다.
'''

#BFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    q = collections.deque([(i, j)])
                    grid[i][j] = '-1'
                    
                    while q:
                        x, y = q.popleft()
                        for dx, dy in (0,1), (1,0), (0, -1), (-1,0):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                                q.append((nx, ny))
                                grid[nx][ny] = '-1'
                    ans += 1
        return ans

#DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        ans = 0
        
        def dfs(x, y):
            nonlocal n, m
            
            if grid[x][y] == '-1':
                return 0
            
            grid[x][y] = '-1'
            if 0<=x-1<m and grid[x-1][y] == '1':
                dfs(x-1, y)
            if 0<=y-1<n and grid[x][y-1] == '1':
                dfs(x, y-1)
            if 0<=x+1<m and grid[x+1][y] == '1':
                dfs(x+1, y)
            if 0<=y+1<n and grid[x][y+1] == '1':
                dfs(x, y+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans+= 1

        return ans