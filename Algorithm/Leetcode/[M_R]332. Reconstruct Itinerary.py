class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = collections.defaultdict(list)
        
        for i in range(len(tickets)):
            if tickets[i][0] in d:
                d[tickets[i][0]].append(tickets[i][1])
            else:
                d[tickets[i][0]] = [tickets[i][1]]
        #print(d)
                
        
        for i in d.items():
            #print(i[1])
            i[1].sort(reverse=True)
            d[i[0]] =i[1] 
            
        #print(d)
        
        route = []
        def visit(airport):
            while d[airport]:
                visit(d[airport].pop())
            route.append(airport)
            
        visit('JFK')
        
        #print(route)
        return route[::-1]
    
'''
Medium
Graph

그래프를 풀어서 정렬해야한다까지는 맞았다.
방문하면서 답을 구해나가야했는데
visit 메소드부터 풀이를 본것이다.
엄청깔끔핟 ㄷㄷ..


일반 딕셔너리에서는 마지막 키값을 넣으면 에러가 났는데
defaultdict와 일반 dict의 차이이다.
없는 key로 접근해도 에러를 뱉지않는다.
defaultdict를 쓰는게 값을 넣는데도 깔끔하다.
사용을 해야할 떄를 잘 정해서 쓰자


'''