from collections import Counter
class Solution:
    def reorganizeString(self, S: str) -> str:
        ans, count_S = [], Counter(S) 
        
        hq = [(-v, k) for k, v in count_S.items()]
        
        heapq.heapify(hq)
        
        n_v, n_k = 0, ''
        
        while hq:
            v, k = heapq.heappop(hq)
            ans += [k]
            if n_v < 0:
                heapq.heappush(hq, (n_v, n_k))
            v += 1
            n_v, n_k = v, k
            
        if len(S) == len(ans):
            return ''.join(ans)
        return ""
    

'''
난이도 Medium

최대힙을 구성해서 풀어야했던 문제
하나씩 빼가면서 문자열을 구성 결국 반복해서 구성이 불가능하면 힙은 멈추고
빼내지 못한 문자가 있게된다.
전체 문장길이와 비교해서 못나온게 존재하면 실패
 
 
'''
