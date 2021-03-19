class Solution:
    def firstUniqChar(self, s: str) -> int:
        alpha_d = {}
        for i in s:
            if i not in alpha_d:
                alpha_d[i] = 1
            else:
                alpha_d[i] += 1
        
        #print(alpha_d)
        idx = -1
        for k in range(len(s)):
            if alpha_d[s[k]] == 1:
                idx = k
                break
        
        return idx