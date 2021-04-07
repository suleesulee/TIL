class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stck_s = []
        stck_t = []
        
        for i in range(len(s)):
            if s[i] == '#':
                if stck_s: 
                    stck_s.pop()
            else:
                stck_s.append(s[i])
        
        for i in range(len(t)):
            if t[i] == '#':
                if stck_t: 
                    stck_t.pop()
            else:
                stck_t.append(t[i])
        
        
        #print(stck_s)
        #print(stck_t)
        if stck_s == stck_t:
            return True
        else:
            return False