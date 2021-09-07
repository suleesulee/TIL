class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero = 0
        if n == 0:
            return 0
        
        temp = math.factorial(n)
        
        while temp % 10 == 0:
            zero += 1
            temp //= 10
        
        return zero