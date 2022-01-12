import sys

def bfs(val):
	q = []
	q.append(val)
	while q:
		e = q.pop()
		
		if visited[e] == 0:
			visited[e] = 1
			bfs(graph[e])
			
			

if __name__ == "__main__":
	t = int(sys.stdin.readline())
	
	for _ in range(t):
		n = int(sys.stdin.readline())
		graph = [0] + list(map(int, sys.stdin.readline().split(' ')))
		visited = [0 for _ in range(len(graph))]
		cnt = 0
		
		#print(graph)

		for i in range(1, len(graph)):
			if visited[i] == 0:
				visited[i] = 1
				bfs(graph[i])
				cnt += 1
				
		#print(visited)
		print(cnt)
		