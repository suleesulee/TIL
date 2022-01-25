import sys

input = sys.stdin.readline

if __name__ == "__main__":
	n = int(input())
	arr = list(map(int, input().split()))
	set_arr = list(set(arr))
	set_arr.sort()
	d = {set_arr[i] : i for i in range(len(set_arr))}
	
	for i in range(len(arr)):
		print(d[arr[i]], end=' ')
	
 '''
 정렬 문제
 set, sort, dic을 잘 알고있다면 풀수있음
 딕셔너리 컴프리핸션
 
 '''