n = int(input())
time = []

for i in range(n):
	time.append(list(map(int, input().split())))
	
time.sort(key=lambda x: (x[1], x[0]))
#print(time)


cnt = 1 
end_time = time[0][1]

for i in range(1, n):
	if time[i][0] >= end_time: 
		cnt += 1
		end_time = time[i][1]

print(cnt)