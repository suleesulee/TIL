import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    before_sector = 0
    sector = []

    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(before_sector, before_sector + temp[0]):
            sector.append(temp[1])
        before_sector += temp[0]
            
    #print(sector)

    before_sector = 0
    for i in range(m):
        temp = list(map(int, input().split()))
        for j in range(before_sector, before_sector + temp[0]):
            sector[j] = temp[1] - sector[j]
        before_sector += temp[0]

    #print(sector)
    
    if max(sector) <= 0:
        print(0)
    else:
        print(max(sector))
        
'''
한참 해멤
구간나누는거 하지않고 그냥 0-100까지 속도 리스트에 넣고
운영속도 빼줘서 최대 값 구해내면됨
-만 나오게 되면 0으로 예외처리
'''