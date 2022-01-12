import sys


if __name__ == "__main__":
	k, n = map(int, sys.stdin.readline().split())
	lan = []
	answer = 0
	
	for _ in range(k):
		temp = int(input())
		lan.append(temp)
		
	l = 1
	r = max(lan)
	
	while l <= r:
		m = (l+r)//2
		temp = 0		
		
		for i in range(len(lan)):
			temp += (lan[i]//m)
		
		if temp >= n:
			l = m + 1
		else:
			r = m - 1
			
	print(r)
		
		