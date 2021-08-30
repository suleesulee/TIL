import sys

k, p ,n = map(int, input().split())

c = p
while n > 1:
   c *= p
   c %= 1000000007
   n -= 1

#print(c)

virus = (k * c) % 1000000007

print(virus)