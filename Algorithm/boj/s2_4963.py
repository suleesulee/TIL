from collections import deque

def bfs(x, y):
	dx = [0, 1, 0, -1, -1, -1, 1, 1]
	dy = [1, 0, -1, 0, 1, -1, -1, 1]
	q = deque()
	m[x][y] = 0
	q.append([x, y])
	while q:
		x, y = q.popleft()
		for k in range(8):
			nx = x + dx[k]
			ny = y + dy[k]

			if 0 <= nx < h and 0 <= ny < w and m[nx][ny] == 1:

				m[nx][ny] = 0
				q.append([nx, ny])
				

	
while True:
	w, h = map(int, input().split())

	if w == 0 and h == 0:
		break
	
	m = []
	cnt = 0

	for _ in range(int(h)):
		m.append(list(map(int, input().split())))
		
	for i in range(int(h)):
		for j in range(int(w)):
			if m[i][j] == 1:
				bfs(i, j)
				cnt += 1
				
	print(cnt)
		


'''
입력이 그냥 input으로 받으면 int형이 아님.. 이것때문에 한참헤맸다.. 
입력을 꼭 int형으로 받았는지 확인이 필요하다.
'''