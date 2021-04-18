class FirstUnique:
    
    def __init__(self, nums: List[int]):
        self.stck = []
        self.d = dict()
        self.uniq = -1
        sorted(nums)
        for i in nums:
            self.stck.append(i)
            if i in self.d:
                self.d[i] += 1
            else:
                self.d[i] = 1
                
        for i in self.d:
            if self.d[i] == 1:
                self.uniq = i
                break
                
        #print(self.stck)
        #print(self.d)

    def showFirstUnique(self) -> int:
        return self.uniq

    def add(self, value: int) -> None:
        self.stck.append(value)
        
        if self.uniq >= value:
            if value in self.d:
                self.d[value] += 1
            else:
                self.d[value] = 1

            for i in self.d:
                if self.d[i] == 1:
                    self.uniq = i
                    break
                else:
                    self.uniq = -1
        else:               
            if value in self.d:
                self.d[value] += 1
            else:
                if self.uniq == -1:
                    self.uniq = value
                self.d[value] = 1
                   

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)