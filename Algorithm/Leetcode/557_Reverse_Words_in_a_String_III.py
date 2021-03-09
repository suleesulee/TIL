class Solution:
    def reverseWords(self, s: str) -> str:
        part = s.split()
        #print(part)
        reverse = []
        for i in range(len(part)):
            reverse += part[i][::-1]
            reverse = ''.join(reverse) + ' '
            
        return reverse[:-1]
        #print(reverse)

#나의 초기답인데 런타임시간이 장난아님 1800ms인데
#리턴을 돌리는 부분에서도 시간잡아먹고 for문안에서 join등이 영향을 끼친듯
#아래는 리트코드에서 솔루션쪽에 나와 비슷하게 푼 분인데
#배열 자체를 리버싱 해서 돌려버리고 마지막에 조인을 했다

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        for i in range(len(words)):
            words[i] = words[i][::-1]
        
        return ' '.join(words)
        