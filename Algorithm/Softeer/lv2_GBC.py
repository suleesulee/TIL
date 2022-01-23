import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    ans = 0
    before_sector = 0

#   [0 50] [50 90] [90 100] 
#   [50][40][30]
    
    sector = []
    speed = []

    for i in range(n):
        temp = list(map(int, input().split()))
        if i == 0:
            sector.append([0, temp[0]])
        elif i == n-1:
            sector.append([sector[-1][1], 100])
        else:
            sector.append([sector[-1][1], sector[-1][1] + temp[0]])

        speed.append(temp[1])

    for _ in range(m):
        temp = list(map(int, input().split()))
        before_sector += temp[0]
        print(before_sector)
        for i in range(len(sector)):
            if sector[i][0]<=before_sector<=sector[i][1]:
                if temp[1] > speed[i]:
                    over_speed = temp[1] - speed[i]
                    ans = max(ans, over_speed)

    
    print(ans)
