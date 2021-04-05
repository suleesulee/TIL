'''
내가 풀던방식과 가장 유사하게 풀은 풀이
스택에 넣고 팝시키는 경우를 계산했는데
재귀적으로 반복을 못해서 해당 답을 보고 무릎을 탁침

'''


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        size = len(s)
        cnt  =1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                cnt += 1
            else :
                cnt = 1
                
            if cnt == k:
                s = s.replace(s[i-k+1:i+1], "")
                return self.removeDuplicates(s, k)
            
        return s