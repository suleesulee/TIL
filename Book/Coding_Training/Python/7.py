import math

def square(a, b):
    return a * b;
def change_meter(feet):
    x = math.pow(feet, 2) * 0.09290304
    return math.sqrt(x)

print("What is the length of the room in feet? ")
length = int(input());
print("What is the width of the room in feet? ")
width = int(input());
print("you entered dimensions of " + str(length) + " feet by " + str(width) + "feet")
sq = square(length, width)
print("this area is\n" + str(sq) + "square feet\n" + str(change_meter(sq)))
