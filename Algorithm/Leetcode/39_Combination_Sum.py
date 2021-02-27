class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(candidates, target, [], res)
        return res
    
    def dfs(self, nums, target, path, res):
        if target < 0:
            #print(path)
            return
        if target == 0:
            #print(path)
            res.append(path)
            return
        for i in range(len(nums)):
            #print(path)
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], res)