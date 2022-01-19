import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(i, j):
    q.append((i,j))
    cnt = 1

    while q:
        x, y = q.pop()
        visited[x][y] = 1

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0<=nx<n and 0<=ny<n:
                if road[nx][ny] == 1 and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += 1
    ans.append(cnt)

if __name__ == "__main__":
    n = int(input())
    road = []
    visited = [[0] * n for _ in range(n)]
    q = []
    ans = []

    for i in range(n):
        temp = list(map(int, input().rstrip()))
        road.append(temp)

    for i in range(n):
        for j in range(n):
            if road[i][j] != 0 and visited[i][j] == 0:
                bfs(i, j)

    ans.sort()
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i])