import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    line = []
    cnt = 0

    temp = str(input())
    for i in range(len(temp)):
        line.append(temp[i])
    
    #p가 로봇 h가 부품
    #print(line)
    for i in range(len(line)):
        if line[i] == 'P':
            flag = 0
            for j in range(i - k, i):
                if j >= 0:
                    if line[j] == 'H':
                        cnt += 1
                        line[j] = 'X'
                        flag = 1
                        break
            
            if flag == 0:
                for j in range(i + 1, i + k + 1):
                    if j < n:
                        if line[j] == 'H':
                            cnt += 1
                            line[j] = 'X'
                            break

    print(cnt)