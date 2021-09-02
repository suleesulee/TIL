class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stck = []
        #비어있으면 넣고
        #다음에 들어온게 더 크면 넣고 작으면 넣지 않는다.
        
        
        stck.append((heights[-1], len(heights)-1))
        for i in range(len(heights)-1, -1, -1):
            if stck[-1][0] < heights[i]:
                stck.append((heights[i], i))
            
        stck.sort(key = lambda x : x[1])
        #print(stck)
        
        ans = []
        for i in range(len(stck)):
            ans.append(stck[i][1])
            
        #print(ans)
        return ans