class Solution:
    def isHappy(self, n: int) -> bool:
       
        mem = set()
        
        while n != 1:
            print([int(i) ** 2 for i in str(n)])
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
                
        return True
        
        #print([int(i) ** 2 for i in str(n)])