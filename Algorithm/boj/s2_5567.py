n = int(input())
m = int(input())

answer = set()
friend = [[] for _ in range(n + 1)]
q = list()

#친구와 친구의 친구
def bfs():
	for i in friend[1]:
		q.append(i)
		answer.add(i)
	while q:
		findFriend = q.pop(0)
		for i in friend[findFriend]:
			answer.add(i)
	
	
for i in range(m):
	f1, f2 = map(int, input().split())
	friend[f1].append(f2)
	friend[f2].append(f1)

#print(friend)

if not friend[1]:
	print(0)
else:	
	bfs()
	print(len(answer) - 1)