class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int: 
        ans, step = 0, 0
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append((i,j))
                    grid[i][j] = -1
                    step = 1
                    while q:
                        x, y = q.popleft()
                        for dx, dy in [(1,0), (0,1), (-1,0), (0, -1)]:
                            nx = dx + x
                            ny = dy + y
                            if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] == 1:
                                grid[nx][ny] = -1
                                step += 1
                                q.append((nx,ny))

                    ans = max(step, ans)
        return ans  
        #print(ans)