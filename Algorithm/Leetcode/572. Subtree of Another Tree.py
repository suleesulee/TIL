'''
dfs 구현이 두번인게 조금 더럽기는 하다
일단 s,t의 dfs를 통해 똑같은 구조가 있는지 찾아내서 비교했다.
'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        s_nums = []
        t_nums = []
        
        def s_dfs(node):
            if not node:
                s_nums.append(None)
                return 0
            s_nums.append(node.val)
            s_dfs(node.left)
            s_dfs(node.right)
            
        def t_dfs(node):
            if not node:
                t_nums.append(None)
                return 0
            t_nums.append(node.val)
            t_dfs(node.left)
            t_dfs(node.right)
            
        s_dfs(s)
        t_dfs(t)
        
        for i in range(len(s_nums)):
            if s_nums[i] == t_nums[0]:
                if t_nums == s_nums[i:len(t_nums)+i]:
                    return True
        
        return False