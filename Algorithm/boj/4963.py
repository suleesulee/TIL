def isRyon(arr):
    return arr == 1

n, k = map(int, input().split(' '))

arr = list(map(int, input().split(' ')))

l, r = 0, 0
answer = 1e9
cnt = 1 if isRyon(arr[0]) else 0

while True:
    if cnt == k:
        answer = min(answer, r - l + 1)
        if isRyon(arr[l]):
            cnt -= 1
        l += 1
    elif cnt < k:
        r += 1
        if r == n:
            break
        if isRyon(arr[r]):
            cnt += 1
    else:
        if isRyon(arr[l]):
            cnt -= 1
        l += 1

if answer == 1e9:
    answer = -1

print(answer)