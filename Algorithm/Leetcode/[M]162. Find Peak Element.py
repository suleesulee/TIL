class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if i == 0:
                if nums[-1] < nums[i] and nums[i+1] < nums[i] :
                    return i
            elif i == len(nums) - 1:
                if nums[i-1] < nums[i] and nums[0] < nums[i]: 
                    return i
            elif nums[i-1] < nums[i] and nums[i+1] < nums[i]:
                    return i

            
        return 0
            
        
# 파이썬은 이진 탐색으로 문제를 풀었다.. 그냥 쭉 탐색해서 피크인것을 찾으면 반환하도록 했다.