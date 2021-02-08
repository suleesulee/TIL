class Cal:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    def mul(self):
        return self.num1 * self.num2
    def div(self):
        return self.num1 / self.num2

print("What is the first number?")
num1 = input(str())
print("What is the second number?")
num2 = input()
int_num1 = int(num1)
int_num2 = int(num2)
c = Cal(int_num1, int_num2)
print(str(int_num1) + " + " + str(int_num2) + " = " + str(c.add()) + "\n" +
str(int_num1) + " - " + str(int_num2) + " = " + str(c.sub()) + "\n" +
str(int_num1) + " * " + str(int_num2) + " = " + str(c.mul()) + "\n" +
str(int_num1) + " / " + str(int_num2) + " = " + str(c.div()) + "\n")
