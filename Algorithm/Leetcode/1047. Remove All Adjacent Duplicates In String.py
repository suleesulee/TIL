'''
2개가 겹치면 바로 날린다.
스택형식으로 이전의 것이 지금의 것과 같으면 
이전의 것을 pop함..

for문에서 string은 그 문자 자체에서 순서대로 돌수도있다는것 잊지말자
'''

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stck = []
        
        for i in S:
            if stck and i == stck[-1]:
                stck.pop()
            else:
                stck.append(i)
                
        return ''.join(stck)
