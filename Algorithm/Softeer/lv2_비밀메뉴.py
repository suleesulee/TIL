import sys

input = sys.stdin.readline

if __name__ == "__main__":
    m, n, k = map(int, input().rstrip().split())
    secret = list(map(int, input().rstrip().split()))
    user_push = list(map(int, input().rstrip().split()))

    if len(user_push) < len(secret):
        print("normal")

    else:
        flag = 0
        for i in range(len(user_push) - len(secret) + 1):
            #print(user_push[i:i+len(secret)])
            if user_push[i:i+len(secret)] == secret:
                print("secret")
                flag = 1
                break
        
        if flag == 0:
            print("normal")