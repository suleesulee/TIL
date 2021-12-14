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

# 들어가는 값이 엄청 큰 문제
# 그냥 떠오른 방식으로 풀면 절대 답이 안나옴 범위를 한참 넘어설듯.
# 처음 곱할때부터 mod를 해서 큰 값이 절대 못나오도록 해야함
# 채점방식이 너무 아무것도 안알려주는것 같음..