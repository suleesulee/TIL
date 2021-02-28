class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        res = []
        for i in strs:
            sorted_strs =  "".join(sorted(i))
            if sorted_strs in d:
                d[sorted_strs].append(i)
            else:
                d[sorted_strs]  = [i]
        
        for i in d.values():
            res.append(i)
        return res