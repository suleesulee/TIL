import sys

def binary_search(val):
	l = 0
	r = n - 1
	
	while l <= r:
		m = (l + r)//2
		if val == note1[m]:
			return 1
		elif val < note1[m]:
			r = m - 1
		else:
			l = m + 1
			
	return 0

if __name__ == "__main__":
	
	t = int(input())
	
	for i in range(t):
		n = int(input())
		note1 = list(map(int, sys.stdin.readline().split(' ')))
		m = int(input())
		note2 = list(map(int, sys.stdin.readline().split(' ')))
		note1.sort()
	
		for value in note2:
			print(binary_search(value))