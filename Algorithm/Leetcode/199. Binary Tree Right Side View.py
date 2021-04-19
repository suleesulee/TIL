# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = []
    
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return
        
        ans =[]
        
        def dfs(node, lev):
            if lev == len(ans):
                ans.append(node.val)
            for next in [node.right, node.left]:
                if next:
                    dfs(next, lev + 1)
                    
        dfs(root, 0)
        return ans