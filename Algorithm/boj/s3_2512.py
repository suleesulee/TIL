import sys

input = sys.stdin.readline

if __name__ == "__main__":
	n = int(input())
	arr = list(map(int, input().rstrip().split()))
	m = int(input())
	arr_sum = sum(arr)
	mid = 0
	ans = []
	
	if arr_sum <= m:
		print(max(arr))
	else:
		arr.sort()
		l = 0
		r = max(arr)
		
		while l <= r:
			yesan = 0
			mid = (l + r) // 2
			
			for i in range(len(arr)):
				if arr[i] <= mid: #중간값보다 작으면
					yesan += arr[i]
				else:
					yesan += mid
			# 130	
			if yesan > m: #예산이 더 큰 경우
				r = mid - 1
			else:
				l = mid + 1
			
		print(r)
			
'''
이진탐색 잘 구현해놓고 
마지막 값구하는것에서 헤맴
왜 r(최대값)이냐에 대한 의문을 풀지못함
'''