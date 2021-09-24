class WordDistance:
    
    def __init__(self, wordsDict: List[str]):
        self.wordMap = {}
        for i, w in enumerate(wordsDict):
            if(w in self.wordMap):
                self.wordMap[w].append(i)
            else:
                self.wordMap[w] = [i]
            
        #print(self.wordMap)

    def shortest(self, word1: str, word2: str) -> int:
        loc1, loc2 = self.wordMap[word1], self.wordMap[word2]
        #print(loc1, loc2)
        l1, l2, = 0, 0
        min_diff = float("inf")
        
        while l1 < len(loc1) and l2 < len(loc2):
            min_diff = min(min_diff, abs(loc1[l1]-loc2[l2]))
            if loc1[l1] < loc2[l2]:
                l1 += 1
            else:
                l2 += 1
        return min_diff
                          
                           


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)


'''
배운것
enumerate 를 이용한 딕셔너리에 인덱스와 값 삽입법
float('inf') 로 무한대 설정(1e9로도 가능했던거 같은데)
최소값을 찾으려 while문 돌리는 부분은 아직도 확실한 이해는 안된다.
하나씩 올라가며 최소값을 찾기위해 비교하는것 같은데 
이중 포문 돌려서 전부 비교하면 오래걸릴까..? 흠.

'''

