import sys

if __name__ == "__main__":
	N = int(input())
	p = list(map(int, sys.stdin.readline().split(' ')))
	p.sort()
	p_len = len(p)
	time = 0
	
	for i in range(len(p)):
		time += p[i] * (p_len - i)

	print(time)