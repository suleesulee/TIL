class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # 정렬
        # 어차피 현재에서 내가 바꿀수있는거 
        
        if len(nums) < 5:
            return 0
        nums.sort()
        
        return min(nums[-1] - nums[3], nums[-2] - nums[2], nums[-3] - nums[1], nums[-4]- nums[0])
    
'''
Medium
Greed 

4개 이하는 0이 나오는거 알았음

정렬 후 
3개 지워야 하니깐 가장 끝값과 최소인 3개를 지운값
이런식이라는데 솔직히 이해는 안간다.
이해가 되는 날이 오겠지..


'''