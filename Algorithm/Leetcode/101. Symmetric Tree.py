'''
한쪽은 오른쪽부터 한쪽은 왼쪽부터 dfs 탐색을해 val을 왼쪽, 오른쪽 리스트에 넣고 
최종적으로 리스트를 비교해서 같으면 True, 다르면 False 리턴
edge case를 생각해야한다.
'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root.right and not root.left:
            return True
        if not root.right or not root.left:
            return False
        
        r_root = root.right
        l_root = root.left
        l_list, r_list = [], []
        
        def l_dfs(node):
            if not node:
                l_list.append(None)
                return 0
            l_list.append(node.val)
            left = l_dfs(node.left)
            right = l_dfs(node.right)
            
        def r_dfs(node):
            if not node:
                r_list.append(None)
                return 0
            r_list.append(node.val)
            right = r_dfs(node.right)
            left = r_dfs(node.left)
            
            
            
        l_dfs(l_root)
        r_dfs(r_root)
        print(l_list)
        print(r_list)
        if r_list == l_list:
            return True
        else:
            return False
        