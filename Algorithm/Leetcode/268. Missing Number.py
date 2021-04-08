'''
수학문제이다.. 
Brute Force로 풀수있지만
수학으로 풀어야 깔끔하게 나온다.
nums의 len을 알아낸뒤 1부터 len까지 더한 결과와 nums의 sum을 빼주면 답이 나오는데
이렇게 풀어야 실행속도가 빠르다.
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        for i in range(n):
            if i not in nums:
                return i