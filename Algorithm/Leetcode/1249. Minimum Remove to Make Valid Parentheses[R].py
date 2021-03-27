'''
비어있는 괄호 처리관련해서 못처리해서
답을 봄
위치를 기억해서 남아있는 괄호를 날려버려야한다.
'''

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    s[i]=""
        #print(s)
        for i in stack:
            s[i] =""
            
        return "".join(s)