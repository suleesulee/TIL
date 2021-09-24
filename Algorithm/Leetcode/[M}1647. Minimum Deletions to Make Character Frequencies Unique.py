class Solution:
    def minDeletions(self, s: str) -> int:
        cnt, ans, used = collections.Counter(s), 0, set()
        
        for ch, fq in cnt.items():
            while fq > 0 and fq in used:
                fq -= 1
                ans += 1
            used.add(fq)
            
        print(used)
        return ans
'''
Medium
Sorting, greedy

소팅을 가장한 그리디 문제.. 당혹스럽지만
몇개인지 카운팅해서 겹치는게 나타나면 줄여나가며 답을 찾는 그런 문제

'''