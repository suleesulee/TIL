#easy
#python3
#two pointer

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0        
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0: 
                nums[slow], nums[fast] = nums[fast], nums[slow]
                
            if nums[slow] != 0: # 따라오는 포인터 증가 0이 아니깐
                slow += 1