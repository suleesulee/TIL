import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    line = []
    for i in range(n-1):
        line.append(list(map(int, input().split())))
    
    work = list(map(int, input().split()))
    #print(line)

    time_a = 0
    time_b = 0

    work_a = 0
    work_b = 0

    for i in range(n-1):
        time_a = min(line[i][0] + work_a, line[i][1] + line[i][3] + work_b)
        time_b = min(line[i][1] + work_b, line[i][0] + line[i][2] + work_a)

        work_a = time_a
        work_b = time_b

    work_a += work[0]
    work_b += work[1]

    print(min(work_a, work_b))