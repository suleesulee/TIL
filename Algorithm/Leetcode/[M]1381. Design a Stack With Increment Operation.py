class CustomStack:
    
    def __init__(self, maxSize: int):
        self.custum_stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.custum_stack) < self.maxSize:
            self.custum_stack.append(x)
        
    def pop(self) -> int:
        if self.custum_stack:
            return self.custum_stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if k <= len(self.custum_stack):
            for i in range(k):
                self.custum_stack[i] += val
        else:
            for i in range(len(self.custum_stack)):
                self.custum_stack[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

'''
Medium
Stack

그냥 스택을 구현하는 문제

'''