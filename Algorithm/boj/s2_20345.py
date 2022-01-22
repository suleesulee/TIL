import sys

input = sys.stdin.readline

if __name__ == "__main__":
	n, q= map(int, input().split())
	arr = []
	visited = set()

	for _ in range(q):
		arr.append(int(input()))
		
	for i in range(q):
		res = 0
		duck = arr[i]
		while duck > 1:
			if duck in visited:
				res = duck
			duck //= 2
		visited.add(arr[i])
		
		print(res)
