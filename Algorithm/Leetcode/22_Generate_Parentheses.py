class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dfs_str = ""
        r, l, ans = n, n, []
        self.dfs(r, l, ans, dfs_str)
        return ans
    
    def dfs(self, r, l, ans, dfs_str):
        if r < l or r == -1 or l == -1:
            return
        
        if l==0 and r==0:
            ans.append(dfs_str)
        
        self.dfs(r - 1, l, ans, dfs_str + ")")
        self.dfs(r, l - 1, ans, dfs_str + "(")