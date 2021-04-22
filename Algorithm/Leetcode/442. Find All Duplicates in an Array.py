class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if nums is None:
            return 
        
        d = {}
        ans = []
        
        for i in range(len(nums)):
            if not nums[i] in d:
                d[nums[i]] = 1
            elif d[nums[i]] == 1:
                d[nums[i]] += 1
                ans.append(nums[i])
        
        return ans