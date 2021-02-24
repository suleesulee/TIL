import math

def cal(width, length):
    square = width * length
    need = math.ceil(square/9)
    return (square, need)

print("width : ")
width = int(input())
print("length : ")
length = int(input())
(square, need) = cal(width, length)

print("You will need to purchase "+ str(need) + "liters of\npaint to cover "+ str(square)+"meters.")