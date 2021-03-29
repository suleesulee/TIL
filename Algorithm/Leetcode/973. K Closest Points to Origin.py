'''
일반적으로 맵핑을 통해 풀려했는데
같은값이 나오는 다른수 (-1, 1) (1, -1)을 극복못하고 마지막 테스트케이스에서 걸려서 실패 아마 부분 점수를 받을듯 코딜리티라면
'''

#solve1 85 tc가 있는데 84번째에서 걸려서 실패함
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mapping = {}
        ans = []
        ans2 = []
        if k == len(points):
            return points
        
        for i in range(len(points)):
            mapping[(math.sqrt(pow(points[i][0]-0, 2) + math.pow(points[i][1]-0, 2)))] = i
            ans.append(math.sqrt(pow(points[i][0]-0, 2) + math.pow(points[i][1]-0, 2)))
        
        print(ans)
        ans.sort()
        
        for i in range(k):
            ans2.append(points[mapping.get(ans[i])])
        
        return ans2
    
        #print(ans2)
        #print(ans)