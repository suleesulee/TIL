class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        start = None
        
        for idx, n in enumerate(nums):
            if start is None:
                start = n
            if idx == len(nums) - 1 or n<nums[idx+1]-1:
                ans.append(str(start)+ "->"+str(n) if start != n else str(n))
                start = None
                
        return ans