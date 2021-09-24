class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        
        total, max_sum, cur_max, min_sum, cur_min = 0, nums[0], 0, nums[0], 0
        
        for num in nums:
            cur_max = max(cur_max + num, num)
            max_sum = max(max_sum, cur_max)
            cur_min = min(cur_min + num, num)
            min_sum = min(min_sum, cur_min)
            total += num
        
        if max_sum > 0:
            return max(max_sum, total - min_sum)
        else:
            return max_sum
        

'''
Medium
Sort


풀이법:
사실상 카데인 알고리즘을 알아야했다
현재의 맥스값 민값을 유지하며 계속해서 맥스sum, 민sum, total을 구하고
max_sum이 0보다 크다면
토탈과 min_sum을 뺸값을 비교하여 큰 값을 반환
max_sum이 0이거나 음수면 max_sum 반환

카데인 알고리즘
num[i] = max(num[i], num[i] + num[i-1])
부분합 최대값 구하는법
'''
