class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        print(set(zip(s,t)))
        
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
    
    
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping1, mapping2 = {}, {}
        index = 0

        for i in s:
            if i in mapping1:
                mapping1[i].append(index)
            else:
                mapping1[i] = [index]
            index+=1

            
        index = 0
        for i in t:
            if i in mapping2:
                mapping2[i].append(index)
            else:
                mapping2[i] = [index]
            index+=1
                
        return sorted(mapping1.values()) == sorted(mapping2.values())