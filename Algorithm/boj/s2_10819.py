import sys
from itertools import permutations

input = sys.stdin.readline

if __name__ == "__main__":
	n = int(input())
	arr = list(map(int, input().split()))
	permu = permutations(arr)
	max_value = 0
	
	for i in permu:
		permu_sum = 0
		for j in range(len(i) - 1):
			permu_sum += abs(i[j]-i[j+1])
		if permu_sum > max_value:
			max_value = permu_sum
			
	print(max_value)
 
 
'''
Brute force문제 
파이썬의 라이브러리를 이용해 순열을 구하고
문제가 원하는 조건에 따라 답을 구해서 반환
'''