import sys

#n:회원수 m: 친분관계

n, m = map(int, input().split())
w = list(map(int, input().split()))
w.insert(0, 0)
d = {}
ans = 0
for i in range(m):
    p, r = map(int, input().split())
    if p in d:
        d[p].append(r)
    else:
        d[p] = [r]
    if r in d:
        d[r].append(p)
    else:
        d[r] = [p]


# print(d.items())
d_list = list(d.items())
#print(d_list, len(d_list))

# print(d_list[1][0])
# print(d_list[1][1])
# print(d_list[1][1][0])


for i in range(len(d_list)):
    p = d_list[i][0]
    best = True
    for j in range(len(d_list[i][1])):
        temp = d_list[i][1][j]
        if w[p] <= w[temp]:
            best = False
            break
    if best == True:
        ans += 1        

if len(d_list) != n:
    ans += n - len(d_list)




print(ans)