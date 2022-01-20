import sys

input = sys.stdin.readline


def pow(n):
    mod = 1000000007
    if n <= 1:
        return (p ** n) % mod
    if n % 2 == 0:
        return (pow(n//2) ** 2) % mod
    elif n % 2 == 1:
        return (p * pow(n//2) ** 2) % mod


if __name__ == "__main__":
    k, p, n = map(int, input().split())

    #0.1초당 P배씩 증가
    #k마리가 있었다면 N초후에는 몇 마리로?
    #1초당 p^30배 증가
    #3초후에는 30배
    virus = (k * pow(n * 10))%1000000007

    print(virus)