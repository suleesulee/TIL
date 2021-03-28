'''
dict을 이용하여 hash를 만들어 푸는게 가장 빠르겠지만
그냥 list만 사용하여 풀음
'''


class MaxStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stck = []
        self.max_num = -987654321
    def push(self, x: int) -> None:
        self.stck.append(x)
        if self.max_num < x:
            self.max_num = x

    def pop(self) -> int:
        pop_val = self.stck[-1]
        self.stck.pop(-1)
        self.findMax()
        return pop_val

    def top(self) -> int:
        return self.stck[-1]

    def peekMax(self) -> int:
        return self.max_num

    def popMax(self) -> int:
        ans = self.max_num
        for i in reversed(range(len(self.stck))):
            if self.stck[i] == self.max_num:
                self.stck.pop(i)
                break
        self.findMax()
        return ans
    
    def findMax(self)->None:
        self.max_num = -987654321
        for i in range(len(self.stck)):
            if self.max_num < self.stck[i]:
                self.max_num = self.stck[i]        
        
        
# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()