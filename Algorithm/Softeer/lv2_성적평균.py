import sys

a=[]
b=[]
n,k = map(int,input().split())
score = list(input().split())
for i in range(0,n):
    score[i]=int(score[i])
for i in range(0,k):
    c,d = map(int,input().split())  
    a.append(c)
    b.append(d)
for i in range(0,k):
    sum=0
    avg=0
    for j in range(a[i]-1,b[i]):
        sum+=score[j]
    avg=sum/(b[i]-a[i]+1)
    print(format(avg,".2f"))
    