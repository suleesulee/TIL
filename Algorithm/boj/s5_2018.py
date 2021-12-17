n = int(input())

l, r = 0, 1
ans = 1
_sum = 1

while l < n//2 + 1:
	if _sum < n:
		r += 1
		_sum += r
	elif _sum == n:
		ans += 1
		_sum -= l
		l += 1
		r += 1
		_sum += r
	else:
		_sum -= l
		l += 1
	
	#print(_sum)
	
print(ans)