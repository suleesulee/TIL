class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        rightmost = {c:i for i, c in enumerate(S)}
        l, r = 0, 0
        print(rightmost)
        
        res = []
        
        for i, letter in enumerate(S):
            r = max(r, rightmost[letter])
            #print(r)
            if i == r:
                res += [r-l+1]
                l = i+1
        
        return res


'''
Medium
Hash, Two pointer

문제 자체를 이해하지 못했다.. 답을 보고도 한참을 이해하지 못함..
나중에 다시풀어보자.
각 문자의 가장 오른쪽에있는 부분을 딕셔너리로 만들고
처음부터 다시탐색..


'''