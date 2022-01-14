import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def djikstra(start):
	distance[start] = 0 
	heapq.heappush(q, (0, start))
	
	while q:
		dist, e = heapq.heappop(q)
		if distance[e] < dist:
			continue
		
		for i in edge[e]:
			cost = dist + i[1]
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))
	
	
if __name__ == "__main__":
	v, e = map(int, sys.stdin.readline().split())
	k = int(sys.stdin.readline())
	
	distance = [INF] * (v+1)
	edge = [[] for _ in range(v+1)]
	q = []

	for _ in range(e):
		e1, e2, w = map(int, sys.stdin.readline().split())
		edge[e1].append((e2, w))
		

	djikstra(k)
	
	for i in range(1, v+1):
		if distance[i] == INF:
			print("INF")
		else:
			print(distance[i])