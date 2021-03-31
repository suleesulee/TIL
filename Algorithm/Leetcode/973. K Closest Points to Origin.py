'''
#solve1 85 tc가 있는데 84번째에서 걸려서 실패함
맵핑을 통해 풀려했는데 같은값이 나오는 다른수 (-1, 1) (1, -1)를 극복못하고 실패
코딜리티라면 아마 부분 점수를 주지않을까

#solve2 lamda를 이용한 풀이 사실 c만쓰다보니 lamda가 익숙치 않다.

#solve3 python의 heap을 이용한 풀이
heapq를 사용하여 최소힙형태로 저장하여 푼다.



'''

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mapping = {}
        ans = []
        ans2 = []
        if k == len(points):
            return points
        
        for i in range(len(points)):
            mapping[(math.sqrt(pow(points[i][0], 2) + math.pow(points[i][1], 2)))] = i
            ans.append(math.sqrt(pow(points[i][0], 2) + math.pow(points[i][1], 2)))
        
        print(ans)
        ans.sort()
        
        for i in range(k):
            ans2.append(points[mapping.get(ans[i])])
        
        return ans2
    
        #print(ans2)
        #print(ans)

#solve2 lamda를 사용한 정렬

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda P:P[0]**2+P[1]**2)
        return points[:k]