from collections import Counter
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = []
        
        for i in range(len(words)):
            d.append(Counter(words[i]))

        da  = Counter()
        for i in range(len(d)):
            da += d[i]
                
        d_list = list(da.items())
        #print(d_list)
        
        n = len(words)
        
        for k, v in d_list:
            #print (k,v)
            if (v%n) != 0:
                return False
        return True
    
# Counter를 사용해서 빼내는법, for문을 통해 딕셔너리에 넣고 빼내는법
# 둘중하나를 사용해서 갯수를 구하면 된다.
# 다음과정에서 생각을 잘못해서 해답을 봤는데
# 각 글자당 갯수가 words의 갯수로 나누어 떨어져야 정답이 나올수있다. 
# 특이하게 배운것
# Counter로 뽑아낸 것은 Counter 객체에만 제대로 담긴다 list dict 이상하게 넣어보려하면 다 실패한다.
# Counter로 뽑아낸 것은 딕셔너리형태지만 합교집합 가능, 그리고 덧셈 뺄셈도 가능
# most_common이나 elements 같은 메소드 들도 가지고 있음