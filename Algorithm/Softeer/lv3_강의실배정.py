import sys
import heapq
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    time = []

    for _ in range(n):
        s, e = map(int, input().split())
        heapq.heappush(time, (e, s))

    v = 0
    count = 0
    print(time)
    
    while time:
        e, s = heapq.heappop(time)

        if s >= v:
            count += 1
            v = e

    print(count)


'''
heapq를 이용하여 최소힙을 사용해
되는 시간부터 가장 작은거를 사용해서 계속 비교해 나간다.
'''