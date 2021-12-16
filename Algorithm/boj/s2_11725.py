import sys
from collections import deque

def findParent():
	q = deque()
	q.append(1)
	while q:
		node = q.popleft()
		for i in tree[node]:
			if parent[i] == 0:
				parent[i] = node
				q.append(i)
			

n = int(input())

tree = [[] for _ in range(n+1)]
parent = [0] * (n+1)

for i in range(n-1):
	p, c = map(int, sys.stdin.readline().split())
	tree[p].append(c)
	tree[c].append(p)

findParent()

for i in range(2, n+1):
	print(parent[i])