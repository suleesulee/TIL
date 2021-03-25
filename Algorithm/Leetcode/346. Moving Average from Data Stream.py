class MovingAverage:
    ans = []
    
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.ans = []

    def next(self, val: int) -> float:
        size, ans = self.size, self.ans
        ans.append(val)
        if len(ans) >= size:
            window_sum = sum(ans[len(ans)-size:])
            return window_sum/size
        else:
            window_sum = sum(ans[:len(ans)])
            return window_sum/len(ans)
            


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)