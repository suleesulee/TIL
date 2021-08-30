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