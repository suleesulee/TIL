class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        #1은 3이부모 3은 0 루트 10은 5가 부모 5는 3이 부모
        self.d = {}
        self.ans = []
        
        for i in range(len(pid)):
            if pid[i] not in self.d:
                self.d[pid[i]] = []
        
        #print(self.d)
        
        for i in range(len(ppid)):
            if ppid[i] != 0:
                self.d[ppid[i]].append(pid[i])
            # else:
            #     d[pid[i]].append(0)
        #print(self.d)
        
        
        def bfs(v):
            if not v:
                return 
            
            for i in v:
                self.ans.append(i)
                bfs(self.d[i])
            
                
            
        
        self.ans.append(kill)
        bfs(self.d[kill])
        
        #print(self.ans)
        return self.ans
    
'''
Medium
Tree bfs

그래프로 변환한 뒤
답이 될수있는 모든 부분을 순회하면서 답에 추가함


'''