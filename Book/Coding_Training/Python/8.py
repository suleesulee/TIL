import math

def pizza_cal(pizza, people, piece):
    each = pizza * piece / people
    leftover = pizza * piece % people

    return (each, leftover)


print("How many People?")
people = int(input())
print("How many pizzas do you have? ")
pizzas = int(input())
print("How many pieces are in a pizza?")
piece = int(input())

(each, lf) = pizza_cal(pizzas, people, piece)

print(str(people) + " people with " + str(pizzas) + "pizzas")
print("Each person gets "+ str(lf) +" pieces of pizza.\n There are "+ str(lf) + " leftover pieces.")