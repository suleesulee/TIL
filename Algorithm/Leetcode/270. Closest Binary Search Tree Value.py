# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    cal = 123456789
    ans = -1

    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root:
            return
        
        
        if abs(root.val - target) < self.cal :
            self.cal = abs(root.val - target)
            self.ans = root.val
        
        
        self.closestValue(root.left, target)
        self.closestValue(root.right, target)
        
        
        return self.ans
        