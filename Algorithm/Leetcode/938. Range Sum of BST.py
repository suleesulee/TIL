'''
이제 이런문제는 그냥 풀어야하지 않겠어요
DFS를 사용 완전탐색해서 조건에 따른 값을 더해서 반환
특이점은 nonlocal 변수정도
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        ans = 0
        
        def dfs(node):
            if not node:
                return 0
            nonlocal ans
            if low <= node.val <= high:
                #print(node.val)
                ans += node.val
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        
        dfs(root)
        
        #print(ans)
        return ans
            