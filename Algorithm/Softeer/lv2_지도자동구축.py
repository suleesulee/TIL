import sys

n = int(input())

k = 2
t = 0
for i in range(n):
    t += (2 ** i)
print((k+t) ** 2)