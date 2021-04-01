'''
파이썬에서 정렬을 사용하면 그냥 풀리는 문제인데.. 흠..
왜 난이도가 미들일까..
다른 방식으로는 힙을 이용하는 방법이 있는데
이방법도 파이썬 힙을 사용하면된다..

'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        #print(nums[k-1])
        return nums[k-1]