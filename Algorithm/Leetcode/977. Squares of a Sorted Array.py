class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[i]**2)
        
        return sorted(ans)