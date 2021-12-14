n = int(input())
ans = 0
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

a.sort()
b.sort(reverse=True)

for i in range(len(a)):
	ans += (a[i] * b[i])
	
print(ans)