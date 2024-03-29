INF = int(1e9)

n = int(input())
m = int(input())


graph = [[INF] * (n+1) for _ in range(n+1)]

print(graph)

#자기 자신에서 자기 자신으로 가는 비용은 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
            
print(graph)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    
print(graph)


for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

            
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INF")
        else:
            print(graph[a][b], end=" ")
    print()            
