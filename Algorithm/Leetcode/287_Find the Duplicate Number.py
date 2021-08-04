import collections
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = collections.Counter(nums)
        #print(d)
        
        ans = list(d.items())
        ans.sort(key=lambda ans: ans[1], reverse=True)
        
        #print(ans)
        return ans[0][0]
        