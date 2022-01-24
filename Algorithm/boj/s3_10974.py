import sys
from itertools import permutations

input = sys.stdin.readline

if __name__ == "__main__":
	n = int(input())
	
	arr = []
	for i in range(n):
		arr.append(i+1)
	
	for a in permutations(arr, len(arr)):
		for number in a:
			print(number, end=' ')
		print()