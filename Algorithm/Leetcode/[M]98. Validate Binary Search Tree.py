class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:        
        ans = []
        self.inorder(root, ans)
        print(ans)
        
        for i in range(1, len(ans)):
            if ans[i] <= ans[i-1]:
                return False
        
        return True
        
        
    def inorder(self, root, ans):
        if not root :
            return
        
        self.inorder(root.left, ans)
        ans.append(root.val)
        self.inorder(root.right, ans)
        
        
            
'''
Medium
Tree

가끔 코테에 트리문제 등장 해당문제는 BST의 특징을 알고있어야 풀 수 있다.
inorder, preorder, postorder만 돌려서 풀어낼 수 있는 문제가 꽤 많음.
방법을 외우자
in이 중간 pre는 앞 post는 뒤
순서는 left, right 순으로 돌아간다.



루트를 기준으로 왼쪽노드는 루트보다 작아야하고 오른쪽은 루트보다 커야한다.
비교할때는 루트 값이 맥스나 민 역할을 해야하며 
재귀... 반복한다.
BST의 구조를 잘 알고있어야함


inorder 탐색으로도 풀어낼 수 있음
사실상 BST의 구조를 알아야 풀어낼수있음

'''