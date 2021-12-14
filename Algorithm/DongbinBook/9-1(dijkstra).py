import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

start= int(input())
#그래프, [연결정점, 가중치]
graph = [[] for i in range(n+1)]
print(graph)

#방문유무
visited = [False] * (n+1)

#거리
distance = [INF] * (n+1)


print(visited)
print(distance)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
        
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                
                
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])