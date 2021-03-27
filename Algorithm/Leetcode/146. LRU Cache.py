'''
LRU를 구현하는 문제
오더드딕셔너리에 키와 값을 넣고
용량이 비어있으면 그냥 넣고
같은게 들어오면 뒤로 옮김 
이유는 용량이 부족하면 앞부터 버릴거라서


'''


class LRUCache:
    
    def __init__(self, capacity: int):
        self.dic = collections.OrderedDict()
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        temp = self.dic.pop(key)
        self.dic[key] = temp
        return temp

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                self.dic.popitem(last = False)

        self.dic[key] = value
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)