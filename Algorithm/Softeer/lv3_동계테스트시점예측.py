import sys

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
inside_q = []
q = []
change = set()

def bfs(i, j):
    q.append((i, j))

    while q:
        x, y = q.pop()
        visited[x][y] = 1
        cnt = 0

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m:
                if ice[nx][ny] == 0:
                    cnt += 1
                if ice[nx][ny] == 1 and visited[nx][ny] == 0:
                    q.append((nx, ny))
            
            if cnt >= 2:
                change.add((x, y))
                

def inside(i, j, cnt):
    inside_q.append((i,j))
    if cnt != 1:
        ice[i][j] = cnt

    while inside_q:
        x, y = inside_q.pop()
        visited[x][y] = 1

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and ice[nx][ny] == 0:
                    inside_q.append((nx, ny))
                    visited[nx][ny] = 1
                    if cnt != 1:
                        ice[nx][ny] = cnt

if __name__ == "__main__":
    n, m = map(int, input().split())

    ice = []
    visited = [[0]*m for _ in range(n)]  
    ans = 0

    for i in range(n):
        temp = list(map(int, input().split()))
        ice.append(temp) 

    #bfs로 순환하면서 없어지는 얼음을 찾아낸다.
    #1. 안에 들어있어서 안 없어지는것 찾아낸다.1차bfs
    #2. 실제로 없어지는거 찾아 내야하는 bfs
    #visited는 계속 초기화가 필요함
    #한번도 들어가지 않는다면 끗

    while 1:
        '''
        seq 1
        '''
        color = 1

        for i in range(n):
            for j in range(m):
                if ice[i][j] == 0 and visited[i][j] == 0:
                    inside(i, j, color)
                    color += 1

        '''
        배열 프린팅
        '''
        # for i in range(n):
        #     print(ice[i])
        
        # print()
        '''
        visited 초기화
        '''
        visited = [[0] * m for _ in range(n)]  

        
        '''
        seq 2
        '''
        for i in range(n):
            for j in range(m):
                if ice[i][j] == 1 and visited[i][j] == 0:
                    bfs(i, j)
        
        '''
        배열 프린팅
        '''
        # for i in range(n):
        #     print(ice[i])

        # print(change)

        '''
        탈출 조건 change될 부분 없음
        '''
        if not change:
            break
        '''
        녹아버리는 부분 처리
        '''
        for i in range(len(change)):
            x, y = change.pop()
            ice[x][y] = 0

        # print()
        # for i in range(n):
        #     print(ice[i])

        '''
        안에 비어있는 부분 처리
        '''
        for i in range(n):
            for j in range(m):
                if ice[i][j] > 1:
                    ice[i][j] = 0
        ans += 1

        visited = [[0]*m for _ in range(n)]  

    print(ans)