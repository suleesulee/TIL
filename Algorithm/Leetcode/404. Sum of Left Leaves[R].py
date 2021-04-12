# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sumNode  = 0    
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def subtree(s_t, is_left):
            if s_t.left is None and s_t.right is None:
                return s_t.val if is_left else 0
            
            total = 0
            if s_t.left:
                total += subtree(s_t.left, True)
            if s_t.right:
                total += subtree(s_t.right, False)
            
            return total
        
        
        return subtree(root, False)