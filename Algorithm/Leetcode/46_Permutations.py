class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            res = list(permutations(nums, len(nums)))
        return res
        