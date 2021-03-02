import sys

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
first = len(arr)-1
second = len(arr)-2

while True:
    for i in range range(k):
        if m == 0:
            break
        res += first
    if  m == 0:
        break
    res += second
    m -= 1

print(res)
