class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # 탐색을 p,q를 찾는다.
        
        # 둘 중 하나가 포함관계이면 상위것을 반환
        
        # 아닌 경우 거슬러 올라가며 공통의 조상을 찾는다.
        path = list()
        
        while p:
            path.append(p)
            p = p.parent 
        
        while q not in path:
            q = q.parent 
        
        return q
        

'''
Medium 문제
Tree 탐색 유형

멍청한 짓을 하다가 제대로 못푼 문제
처음에 p, q 연결된거 다 구해서 비교해려했다.
사실 한쪽만구해서 반대쪽은 그것에 기반해서 거슬러 올라가면 되는거였는데 바보짓을했다
처음 풀이는 상당히 난해하고 조건이 엄청 달려서 이거 이상한데 했었다.
테스트케이스 31중에 30가서 막히는경우도 있었고 상당히 당황했음


'''