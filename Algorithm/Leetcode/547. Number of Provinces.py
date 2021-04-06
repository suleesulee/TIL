class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visit = [0] * n
        ans = 0
        q = [] 

        
        for i in range(n):
            if not visit[i]:
                q.append(i)
            
                while q:
                    f = q.pop(0)
                    visit[f] = True;
                    
                    for j in range(n):
                        if isConnected[f][j] and visit[j] == 0:
                            q.append(j)
                ans += 1
        
        
        return ans            