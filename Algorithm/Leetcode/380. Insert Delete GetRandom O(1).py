'''
단지 나는 리스트하나에 의존해서 풀었는데
정확한 O(1)의 풀이는 딕셔너리까지 사용해 해시테이블을 가지고 풀어야한다
음.. 일단 O(1)에 푸는게 목적이었으니..
해시테이블 사용이 맞다 나는 O(n)이니
'''

class RandomizedSet:
    random = []
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.random = []
        #, self.pos = [], {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.random:
            return False
        else:
            self.random.append(val)
            #self.pos[val] = len(self.random) - 1
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.random:
            self.random.remove(val)
            return True
            #idx = self.pos[val]
            
            #last = self.random[-1]
            #self.random[idx] = last
            #self.pos[last] = idx
            #self.random.pop()
            #self.pos.pop(val)
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.random)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()