class Solution:
    def isThree(self, n: int) -> bool:
        cnt = 1
        for i in range(2, n+1):
            if n%i == 0:
                cnt+=1
            
            if cnt>3:
                return False
            
        if cnt == 3:
            return True

# 너무 쉬운 문제가 아닌가 싶다
# 트릭이 딱히 없다