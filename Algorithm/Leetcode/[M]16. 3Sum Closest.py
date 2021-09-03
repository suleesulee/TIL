class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = 1e9
        nums = sorted(nums)
        
        for i in range(len(nums)):
            s, e = i + 1, len(nums)-1
            while s < e:
                sum = nums[i] + nums[s] + nums[e]                
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    s += 1
                else:
                    e -= 1
            if diff == 0:
                break
                    
        return target - diff


'''
투포인터문제

정렬하고 범위 줄여가면서 계산한다.

'''