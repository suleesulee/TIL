class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        eMap = {e.id:e for e in employees}
        
        
        print(eMap)
        def dfs(eid):
            employee = eMap[eid]
            return employee.importance + sum(dfs(eid) for eid in employee.subordinates)
        return dfs(id)