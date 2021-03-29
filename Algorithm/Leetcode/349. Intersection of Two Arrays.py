'''
Set을 이용해서 중복 제거 후 교집합연산을 통해 답을 내면됨
'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_num1 = set(nums1)
        set_num2 = set(nums2)
        ans = list(set_num1 & set_num2)
        
        return ans