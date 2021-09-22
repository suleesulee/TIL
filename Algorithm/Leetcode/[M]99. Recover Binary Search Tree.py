# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ans = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)

        inorder(root)
        #print(ans)
        
        
        ans_tmp = ans.copy()
        ans_tmp.sort()
        change = []
        
        for i in range(len(ans)):
            if ans[i] != ans_tmp[i]:
                change.append(ans[i])
                
        #print(change)
        
        def recover(node, cnt):
            if not node:
                return
            if node.val == change[0] or node.val == change[1]:
                if node.val == change[0]:
                    node.val = change[1]
                else: 
                    node.val = change[0]
                cnt -= 1
                if cnt == 0:
                    return
            recover(node.left, cnt)
            recover(node.right, cnt)
        
        recover(root, 2)
        
        #print(root)
'''
Medium
Tree(BST)

이진 탐색트리의 특징 인오더로 돌면 정렬된 값이 나오는 것을 이용한 풀이
한바퀴 돌아온 값과 그 값을 정렬시킨 값을 비교해서 차이나는 부분을 찾고

해당 노드의 값을 바꾸기 위해 돌린다.
딱 2개만 순서를 바꾸면 답을 구할수있는 문제이기에 간단하게 풀 수있음



'''