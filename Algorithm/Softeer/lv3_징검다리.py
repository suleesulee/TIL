import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    stone = list(map(int, input().split()))
    ans = [1] * n

    for i in range(n):
        max_v = 0
        for j in range(i):
            if stone[j] < stone[i]:
                if max_v < ans[j]:
                    max_v = ans[j]

        ans[i] = max_v + 1 
    
    print(max(ans))