import sys

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
find_q = []

def find_start(i, j):
    cnt = 0
    x, y = find_q.pop()

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or nx >= n:
            cnt += 1
        
        if ny < 0 or ny >= m:
            cnt += 1

        if 0 <= nx < n and 0 <= ny < m:
            if robot_map[nx][ny] == '.':
                cnt += 1
    if cnt == 3:
        return True
    else:
        return False

def ch_dir(d, k):
    # 북 -> 동 서, 남-> 동,서 동-> 남 북
    if d == 0:
        if k == 2:
            ans.append('R')
            return 2
        else:
            ans.append('L')
            return 3
    elif d == 1:
        if k == 2:
            ans.append('L')
            return 2
        else:
            ans.append('R')
            return 3
    elif d == 2:
        if k == 0:
            ans.append('L')
            return 0
        else:
            ans.append('R')
            return 1
    else:
        if k == 0:
            ans.append('R')
            return 0
        else: 
            ans.append('L')
            return 1

def bfs(i, j):
    direction = -1  # 0 동 | 1 서 | 2 북 | 3 남
    find_q.append((i, j))
    #방향 찾기
    for k in range(4):
        dir_x = i + dx[k]
        dir_y = j + dy[k]
        if 0 <= dir_x < n and 0 <= dir_y < m:
            #print(robot_map[dir_x][dir_y], dir_x, dir_y)
            if robot_map[dir_x][dir_y] == '#':
                if k == 0:
                    print('>')
                    direction = 0
                elif k == 1:
                    print('<')
                    direction = 1
                elif k == 2:
                    print('v')
                    direction = 2
                else:
                    print('^')
                    direction = 3

    #print(direction)

    #2개 이상 가야하는 점에 #이 있는지 찾기
    while find_q:
        x, y = find_q.pop()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            dou_x = x + (dx[k] * 2)
            dou_y = y + (dy[k] * 2)

            if 0 <= nx < n and 0 <= ny < m:
                #방향이 같은지 확인 
                if direction == k and robot_map[nx][ny] == '#':
                    ans.append('A')
                    robot_map[x][y] = '.'
                    robot_map[nx][ny] = '.'
                    find_q.append((dou_x, dou_y))
                #아니라면 방향을 수정
                elif direction != k and robot_map[nx][ny] == '#':
                    #방향 수정 후 진행
                    #print(direction, k)
                    direction = ch_dir(direction, k)
                    #print(direction, k)
                    ans.append('A')
                    robot_map[x][y] = '.'
                    robot_map[nx][ny] = '.'
                    find_q.append((dou_x, dou_y))

if __name__ == "__main__":
    n, m = map(int, input().split())
    robot_map = [list(input().rstrip()) for _ in range(n)]
    start_idx = []
    ans = []
    #print(robot_map)

    for i in range(n):
        start_tf = False
        for j in range(m):
            if robot_map[i][j] == '#':
                find_q.append((i ,j))
                start_tf = find_start(i, j)

                if start_tf == True:
                    #print(i, j)
                    start_idx.append((i,j))
   
    #print(start_idx)

    find_q.clear()
    print(start_idx[1][0] + 1, start_idx[1][1] + 1)
    
    bfs(start_idx[1][0], start_idx[1][1])    
    answer =''.join(ans)
    print(answer)
            



'''
생각의 흐름

1. 시작점을 찾아야한다. => 한쪽면만 길과 맞다아야함 모서리에 있다면 모시리를 같이 카운트
2. 4방향에 이동경로가 있어야한다.
3. 기존에 따라온 길은 못가게 해야함
4. 현재 방향을 기록하고 방향이 변하면 기록해야함
'''

'''
풀긴했지만 너무오래걸렸다
2시간정도 쓴거 같은데
문제푸는 체력? 이라고해야하나 이런부분이 떨어지는 것 같다. 
많은 연습빼고는 답이 없음

동서남북 표시에 대한 부분에서 헤맸고 경계를 넘어가는 값들은 처음부터 쳐내자
쳐내지 않고 풀다가 경계에서 이상한 값이 튀어나오는데 
디버깅 하는데 시간이 너무 걸렸다.

'''