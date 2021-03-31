class TimeMap:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        getDic = self.dic[key]
        length = len(getDic)
        
        l, r = 0, length
        
        while l < r:
            mid = (l+r) // 2
            if getDic[mid][0] <= timestamp:
                l = mid + 1
            elif getDic[mid][0] > timestamp:
                r = mid
            
        return "" if r == 0 else getDic[r-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)