t = int(input())

for i in range(t):
	n, m = map(int, input().split())
	national = [[] for _ in range(n+1)]
	
	for i in range(m):
		t1, t2 = map(int, input().split())
		national[t1].append(t2)
		national[t2].append(t1)
		
	#print(national)
	visited = [0] * (n+1)
	
	def dfs(idx, cnt):
		visited[idx] = 1
		for i in national[idx]:
			if visited[i] == 0:
				cnt = dfs(i, cnt+1)
				
		return cnt
	
	res = dfs(1, 0)
	print(res)