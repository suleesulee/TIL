class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [] 
        l, r = 0, 0
        cnt = 0
        
        while l < len(T)-1:
            if T[l] >= T[r]:
                r += 1
                cnt += 1

            else:
                l += 1
                r = l
                ans.append(cnt)
                cnt = 0
                
            if r == len(T):
                ans.append(0)
                l += 1
                r = l
                cnt = 0
                
        ans.append(0)
                
        #print(ans)
        return ans



        class Solution:
        def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        stck = [] 
        
        for idx, x in enumerate(T):
            print(idx, x)
            while stck and x > T[stck[-1]]:
                i = stck.pop()
                ans[i] = idx - i
            stck.append(idx)
            
        return ans