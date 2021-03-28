'''
총체적 난국의 문제
여러 방법을 고안해 냈으나 뭐하다보면 걸리고 뭐하다보면 걸려서..
결국 discuss확인 가장 이상적인 답을 찾아 그대로 써보고 생각해봄
00110011
2 2 2 2
min(2, 2), min(2, 2), min (2, 2)
2 + 2 + 2=6
'''

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s += " "
        cnt = 1
        ans = []
        
        for i in range(len(s)-1):
            if s[i+1] == s[i]:
                cnt += 1
            else:
                ans.append(cnt)
                cnt = 1
        
        res = 0
        
        if len(ans)==1:
            return res
        else:
            for i in range(len(ans)-1):
                res += min(ans[i], ans[i+1])
                
            return res