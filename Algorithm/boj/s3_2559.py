import sys

if __name__ == "__main__":
	n, k = map(int, sys.stdin.readline().split(' '))

	ondo = list(map(int, sys.stdin.readline().split(' ')))
	
	ondo_sum = sum(ondo[:k])
	
	l, r = 0, k-1
	answer = ondo_sum
	
	while r < n-1:
		r += 1
		ondo_sum += ondo[r]
		ondo_sum -= ondo[l]
		l += 1
		answer = max(answer, ondo_sum)
		
	print(answer)