class Solution:
    def minOperations(self, s: str) -> int:
        s_len = len(s)
        cnt1, cnt2 = 0, 0
        for i in range(s_len):
            if i % 2 == 1: 
                if s[i] == '1':
                    cnt1 += 1
            else:
                if s[i] == '0':
                    cnt1 += 1
                    
        for i in range(s_len):
            if i % 2 == 1:
                if s[i] == '0':
                    cnt2 += 1
            else:
                if s[i] == '1':
                    cnt2 += 1
                    
        return min(cnt1, cnt2)