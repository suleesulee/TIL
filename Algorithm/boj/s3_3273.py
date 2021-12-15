n = int(input())
arr = list(map(int, input().split(' ')))
x = int(input())

arr.sort()

l, r = 0, n - 1
ans = 0

while l < r:
	if arr[l] + arr[r] < x:
		l += 1
	elif arr[l] + arr[r] > x:
		r -= 1
	else:
		ans += 1
		l += 1
		
print(ans)

'''
간단한 투포인터 문제
정렬 후 해당 조건을 찾아나간다.

'''