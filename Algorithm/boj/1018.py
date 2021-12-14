n, m = map(int, input().split())

map = []
answer = 64

for _ in range(n):
    map.append(input())
    
for i in range(n - 7):
    for j in range(m - 7):
        bw = 0
        wb = 0
        for k in range(8):
            for l in range(8):
                if (k+l)%2 == 0 and map[i+k][j+l] != 'B':
                        bw += 1
                elif(k+l)%2 == 1 and map[i+k][j+l] != 'W':
                        bw += 1
                wb = 64 - bw
        answer = min(answer, wb, bw)
print(answer)