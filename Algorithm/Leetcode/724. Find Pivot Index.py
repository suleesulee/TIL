'''
solve 1은 첫풀이.. 시간이 꽤걸린다. 
계속해서 새로운 덧셈을 수행하는 구조이기 때문
solve2
전체 합을 구한뒤 왼쪽 합을 늘려가며 구함 왼쪽합과 피벗을 빼나가는형식으로 진행 
'''

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, 0
        for i in range(len(nums)):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i+1:])
            if left_sum == right_sum:
                return i
            
        return -1


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum, sum_nums = 0, 0
        sum_nums = sum(nums)
        for i in range(len(nums)):
            if left_sum == sum_nums - left_sum - nums[i]:
                return i
            left_sum += nums[i]
            
        return -1
        