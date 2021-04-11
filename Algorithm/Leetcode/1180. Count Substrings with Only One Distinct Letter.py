'''
사실상의 수학 문제다.
이전의 글자와 현 글자가 같으면 substring이 total에 더할 때 +1 된다.
상기사항이 아닐 경우 다시 1부터 시작
'''
class Solution:
    def countLetters(self, S: str) -> int:
        ans = 1
        temp = 1
        for i in range(1, len(S)):
            if S[i] == S[i-1]:
                temp +=1
                #print(temp)
            else:
                temp = 1
                
            ans += temp
                
        return ans