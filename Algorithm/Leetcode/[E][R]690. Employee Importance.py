class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        eMap = {e.id:e for e in employees}
        
        
        print(eMap)
        def dfs(eid):
            employee = eMap[eid]
            return employee.importance + sum(dfs(eid) for eid in employee.subordinates)
        return dfs(id)
    
# e.id 같은 부분이 구현되어있었고 가져다 쓰면되는거였는데 이해를 못했었고    
# 반복을 돌아야하는 것은 알고있었는데 어떤식으로 돌려야할지 고민했다. 
# dfs
# 해당 풀이는 딕셔너리 컴프리핸션을 사용했는데 익혀야할 테크닉이라고 생각된다.