# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:

        def dfs(node):
            # 노드가 없거나 값이 p또는 q 이면 node 리턴.
            # 처음에 노드가 없으면 그냥 꽝.. p나 q가 처음에 리턴되면..p,q가 lca인거
            
            if not node or node.val == p or node.val == q:
                return node
            
            #왼쪽 오른쪽노드를 집어넣음
            left = dfs(node.left)
            right = dfs(node.right)
            #post로 오른쪽 왼쪽 있으면 node 리턴
            if left and right:
                return node
            #없으면 left, right 리턴.
            else:
                return left or right
        
        def dist(node, target):
            if not node:
                return float('inf')
            if node.val == target:
                return 0
            return 1 + min(dist(node.left, target), dist(node.right, target))      
        
        lca = dfs(root)

        #print(lca)
        return dist(lca, p) + dist(lca, q)



'''
Medium

Binary Tree, DFS

접근법 자체에서 막혔다.
그래프로 해결하려했는데 흠... visited 하나두고 하면 가능했을려나
최신문제여서 해답이 영 시원치 않았다.

Postorder로 lca(공통의 부모인 노드)를 찾아서
해당 노드부터 p,q가 떨어진 길이를 구하는 방식인데
재귀 부분이 잘 이해가 안된다.

나중에 한번 더 풀어볼 문제

'''