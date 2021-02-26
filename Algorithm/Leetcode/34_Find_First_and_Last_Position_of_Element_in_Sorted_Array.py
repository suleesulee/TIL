class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, 1]
        first = self.leftBinarySearch(nums, 0, len(nums)-1, target)
        last = self.rightBinarySearch(nums, 0, len(nums)-1, target)
        return [first, last]
        
        
    def leftBinarySearch(self, nums, l, r, target):
        res = -1
        while l<=r:
            mid = (l + r)//2
            if nums[mid] == target:
                res = mid
                r = mid - 1
            elif nums[mid] > target:
                r = mid - 1 
            else:
                l = mid + 1
        return res
                
    def rightBinarySearch(self, nums, l, r, target):
        res = -1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                res = mid
                l = mid +1 
            elif nums[mid] > target:
                r = mid - 1 
            else:
                l = mid + 1
        return res