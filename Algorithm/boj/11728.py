n, m = map(int, input().split(' '))


arr1 = input().split(' ')
arr2 = input().split(' ')

for i in range(n):
    arr1[i] = int(arr1[i])
for i in range(m):
    arr2[i] = int(arr2[i])

arr = arr1 + arr2
arr.sort()

for i in range(len(arr)):
    print(str(arr[i]) + ' ', end='')