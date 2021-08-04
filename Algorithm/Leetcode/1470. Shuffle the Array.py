class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left, right = [], []
        ans = []
        for i in range(len(nums)):
            if i < n:
                left.append(nums[i])
            else:
                right.append(nums[i])
        for i in range(n):
            ans.append(left[i])
            ans.append(right[i])
        
        return ans
        