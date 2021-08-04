/*
// Definition for Employee.
class Employee {
    public int id;
    public int importance;
    public List<Integer> subordinates;
};
*/

class Solution {
    Map<Integer, Employee> eMap = new HashMap<>();
    
    public int getImportance(List<Employee> employees, int id) {
        for(Employee employee: employees){
            eMap.put(employee.id, employee);
        }
        return dfs(id);
        
    }
    
    public int dfs(int id){
        Employee employee = eMap.get(id);
        int ans = employee.importance;
        for(Integer sub :employee.subordinates)
            ans += dfs(sub);
        return ans;
    }
}