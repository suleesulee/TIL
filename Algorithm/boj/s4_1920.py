n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()

m = int(input())
arr2 = list(map(int, input().split(' ')))

def binary(tmp):
	s, e = 0, n-1
	
	while s <= e:
		mid = (s + e) // 2
		if arr[mid] == tmp:
			return True
		
		if tmp < arr[mid]:
			e = mid - 1
		elif tmp > arr[mid]:
			s = mid + 1


for i in range(m):
	if binary(arr2[i]):
		print(1)
	else:
		print(0)