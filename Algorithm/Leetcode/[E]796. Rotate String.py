class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            s = s[1:] + s[0]
            if s == goal:
                return True
            
        return False
    
# 간단한 문제 str을 쪼개는 방식으로 해당 값이 나오는지 확인했다
# 해당 방법보다 더 나은 방식으로 푸는 방법도 존재했다. 
# s + s 를해서 goal이 그 안에 있는지 확인하는방법