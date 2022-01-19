import sys

b = list(map(int, input().split()))
cnt = 0
if b[0] == 1:
    for i in range(len(b)):
        if b[i] == i+1:
            cnt += 1
    if cnt == 8:
        print("ascending")
    else:
        print("mixed")

elif b[0] == 8:
    for i in range(len(b)):
        if b[i] == len(b)-i:
            cnt+=1
    if cnt == 8:
        print("descending")
    else:
        print("mixed")

else:
    print("mixed")
    
# 현대자동차 그룹의 코딩테스트하는곳 softeer에서 푼 문제
# 리트코드만 풀다보니 심히 당황스럽다 입력을 내가 처리해야해서
# 문제들이 난이도가 널뛰기가 심하고 가독성이 별로라 이해하는데 시간이 좀 걸린다.
# 현대자동차 그룹에서도 자체적으로 코딩테스트를 하고 싶어하는 느낌이다.
# 사이트를 둘러보니 인증제도 하는거 같다.