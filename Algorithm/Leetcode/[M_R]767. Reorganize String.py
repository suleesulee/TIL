class Solution:
    def reorganizeString(self, S: str) -> str:
        ans, c = [], Counter(S)
        hq = [(-value, key) for key, value in c.items()]
        heapq.heapify(hq)
        
        n_v, n_k = 0, ''
        while hq:
            v, k = heapq.heappop(hq)
            ans += [k]
            if n_v < 0:
                heapq.heappush(hq, (n_v, n_k))
            v += 1
            n_v, n_k = v, k
            
        ans = ''.join(ans)
        if len(ans) != len(S):
            return ""
        else:
            return ans;
        
'''
 고민하다가 못풀고 답을 본 문제
 
 heapq의 사용법을 배웠다.. heaqp는 최소힙을 반환 리스트를 넣으면 알고리즘에 따라 정렬해준다.
 
 set으로 여러 값을 한번에 넣으면 맨처음 것을 기준으로 정렬한다. 
 
 maxheap을 만드는 스킬로 -로 값을 넣고 뺄때 다시 -를 붙여주면 최대힙으로 정렬되어 나온다.
 
 문제풀이의 테크닉중 하나를 뽑고 기록해두었다가. 
 다음 것을 뽑고 기록해둔 것을 다시 힙에 넣는다..
 안겹치게 뽑아낼수있을것 같은데..
 
 아직도 솔직히 답이 어떻게 나오는거여 하며 헷갈린다
 못만드는 경우는 리스트에서 다 못뽑아내는건가?!?!
 .. 새벽1시 졸려서 이해가 잘 안된다.
 
 기회가 된다면 언젠가 다시풀어보자
 
'''
