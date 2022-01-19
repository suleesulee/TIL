import sys

w, n = map(int, input().split())
l = [0 for i in range(n+1)]
ans = 0

for i in range(n):
    m, p = map(int, input().split())
    l[p] += m

cnt = len(l) - 1

while w > 0:
    # 담는 무게가 가방보다 큼
    if w < l[cnt]:
        ans += (w * cnt)
        w -= w
    else:
        ans += cnt * l[cnt]
        w -= l[cnt]

    cnt -= 1

print(ans)