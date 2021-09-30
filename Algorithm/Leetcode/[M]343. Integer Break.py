class Solution:
    def integerBreak(self, n: int) -> int:
        if n ==2 or n ==3:
            return n-1
        elif n%3 == 0:
            return 3**(n//3)
        elif n%3 == 1:
            return 3**(n//3 -1)*4
        else:
            return 3**(n//3)*2
        
'''
Medium
DP

3이 들어가는 것이 곱했을때 가장크다는 것으로 유추해서 풀어나감


'''