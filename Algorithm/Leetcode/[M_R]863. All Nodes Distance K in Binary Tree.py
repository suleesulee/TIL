class Solution(object):
    def distanceK(self, root, target, K):
        graph = collections.defaultdict(set)
        self.build_graph(root, None, graph)
        print(graph)
        return self.bfs(graph, target.val, K)
    
    def build_graph(self, root, father, graph):
        if not root:
            return  
        for node in [father, root.left, root.right]:
            #부모의 밸류도 넣고 양옆의 밸류도 넣음
            if node:
                graph[root.val].add(node.val)
                
        if root.left:
            self.build_graph(root.left, root, graph)
        if root.right:
            self.build_graph(root.right, root, graph)
                
    def bfs(self, graph, val, k):
        q = collections.deque([val])
        distance = {val:0}
        ans = []

        while q:
            node = q.popleft()
            if distance[node] == k:
                ans.append(node)
            
            print(distance)
            for neigh in graph[node]:
                if neigh in distance:
                    continue
                q.append(neigh)
                distance[neigh] = distance[node] + 1
        return ans


'''
Medium

Tree, BFS

target에서 k만큼 떨어진 노드를 구하는 문제
그래프로 풀어내고
bfs로 돌린다.
부모와 양옆노드를 추가하고
계속해서 그래프를 만들어낸다

bfs로 돌릴때 한번 방문한 값은 (딕셔너리에 키가 있는)
다시 방문하지 않도록 제한을 둔다.


'''