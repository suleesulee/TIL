'''
루트부터 dfs를 사용해 뒤집어주면 된다.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = root.right, root.left
            if root.left:
                self.invertTree(root.left)
            if root.right:
                self.invertTree(root.right)
        
            return root
        
        else:
            return None
    