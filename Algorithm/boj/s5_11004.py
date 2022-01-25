import sys

input = sys.stdin.readline

if __name__ == "__main__":
	n, k = map(int, input().split())
	arr = list(map(int, input().split()))
	
	#print(arr)
	arr.sort()
	print(arr[k-1])
 
 '''
 간단한 문제 정렬 후 
 문제에서 출력하라는데로 출력하면됨
 '''