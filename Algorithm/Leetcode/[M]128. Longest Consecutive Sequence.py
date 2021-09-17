class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        
        
        long = 0
        curr = 1
        #print(nums)
        for i in range(len(nums)):
            if nums[i] == nums[i-1] + 1:
                #print("IN")
                curr += 1
            elif nums[i] == nums[i-1]:
                pass
            else:
                curr = 1
            
            long = max(long, curr)

        
        return long
       # print(long)