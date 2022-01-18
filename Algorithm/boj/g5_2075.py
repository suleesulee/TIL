import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
	n = int(input())
	arr = []
	heap = []

	
	for _ in range(n):
		arr = list(map(int, input().split()))

		if not heap:
			for ar in arr:
				heapq.heappush(heap, ar)
		else:
			for ar in arr:
				if heap[0] < ar:
					heapq.heappush(heap, ar)
					heapq.heappop(heap)
				
	print(heap[0])


#기본적으로 그냥 리스트에 넣고 정렬해서 찾는것은 안된다.
#파이썬의 힙큐를 이용하여 n개만 넣는다.
