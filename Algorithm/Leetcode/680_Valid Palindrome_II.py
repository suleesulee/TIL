class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        
        else:
            i, j = 0, len(s)-1
            while i<j:
                if s[i] == s[j]:
                    i+=1
                    j-=1
                    continue
                else:
                    right = s[0:j]+s[j+1:]
                    left = s[0:i]+s[i+1:]
                    break
                    
            if right == right[::-1] or left == left[::-1]:
                return True
        
            else:
                return False