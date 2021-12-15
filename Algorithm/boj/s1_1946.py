import sys

t = int(input())

for i in range(t):
	n = int(input())
	
	arr = []
	for j in range(n):
		arr.append(list(map(int, sys.stdin.readline().split())))
	
	arr = sorted(arr, key = lambda x: x[0])

	Max = arr[0][1]
	cnt = 1
	
	for i in range(1, n):
		if Max > arr[i][1]:
			cnt += 1
			Max = arr[i][1]
	
	print(cnt)
		