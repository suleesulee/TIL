import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 1
end = max(tree)

#가장 큰 값을 구하기 위한 
while start <= end:
	mid = (start + end)//2
	answer = 0

	for i in tree:
		if i >= mid:
			answer += i - mid
			if answer > m:
				break
	
	if answer >= m:
		start = mid + 1
	else:
		end = mid - 1

print(end)