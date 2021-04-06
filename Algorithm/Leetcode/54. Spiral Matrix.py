class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        visit = [[0]* n for _ in matrix]
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        d = 0
        q = deque([(0, 0)])
        visit[0][0] = -1
        ans = []
        ans.append(matrix[0][0])
        cnt = 1
        
        while cnt != m * n:
            x, y = q.popleft()
            if d == 0:
                nx = x + dx[0]
                ny = y + dy[0]
                if 0<=nx<m and 0<=ny<n and visit[nx][ny] == 0:
                    visit[nx][ny] = -1
                    q.append((nx, ny))
                    ans.append(matrix[nx][ny])
                    cnt +=1
                else:
                    d = 1
                    q.append((x, y))

            elif d == 1:
                nx = x + dx[1]
                ny = y + dy[1]
                if 0<=nx<m and 0<=ny<n and visit[nx][ny] == 0:
                    visit[nx][ny] = -1
                    q.append((nx, ny))
                    ans.append(matrix[nx][ny])
                    cnt +=1
                else:
                    d = 2
                    q.append((x, y))
                
            elif d == 2:
                nx = x + dx[2]
                ny = y + dy[2]
                if 0<=nx<m and 0<=ny<n and visit[nx][ny] == 0:
                    visit[nx][ny]= -1
                    q.append((nx, ny))
                    ans.append(matrix[nx][ny])
                    cnt +=1
                else:
                    d = 3
                    q.append((x, y))
            else :
                nx = x + dx[3]
                ny = y + dy[3]
                if 0<=nx<m and 0<=ny<n and visit[nx][ny] == 0:
                    visit[nx][ny]= -1
                    q.append((nx, ny))
                    ans.append(matrix[nx][ny])
                    cnt +=1
                else:
                    d = 0
                    q.append((x, y))
            
        return ans
                