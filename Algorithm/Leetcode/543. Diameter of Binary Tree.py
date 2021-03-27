# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        d = 0
        def dfs(node):
            if not node:
                return 0
            nonlocal d

            left = dfs(node.left)
            right = dfs(node.right)
            print(left, right)
            d = max(d, left+right)

            return max(left, right) + 1

        dfs(root)
        return d