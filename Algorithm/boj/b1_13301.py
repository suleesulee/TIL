n = int(input())

dp = []
dp.append(1)
dp.append(2)

if n < 2:
	print(4)

else:
	for i in range(2, 80):
		dp.append(dp[i-2] + dp[i-1])
	
	print((dp[n-1]+dp[n-2]) * 2)