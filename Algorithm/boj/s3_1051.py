n, m = map(int, input().split())
answer = 0
arr = []

for i in range(n):
    arr.append(list(input()))

it = min(n, m)

for i in range(n):
	for j in range(m):
		for k in range(it):
			if ((i + k) < n) and ((j + k) < m) and (arr[i][j] == arr[i][j + k] == arr[i + k][j] == arr[i + k][j + k]):
				answer = max(answer, (k+1)**2)
print(answer)