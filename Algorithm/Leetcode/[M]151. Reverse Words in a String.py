class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        #print(s)
        s.reverse()
        #print(s)
        
        return ' '.join(s)
    

'''
Medium

그냥 사용할 줄 아는 함수가 많으면 장땡인 문제

'''