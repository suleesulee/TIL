import bisect
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7

        nums1, nums2 = zip(*sorted(zip(nums1, nums2)))   
        # zip으로 num1, num2를 한쌍으로 묶고 num1을 기준으로 sort
        # 언패킹연산자 써서 zip을 사용하면 다시 분리됨 (이거 새로 배움)
        
        #리스트 컴프리핸션처리 
        diff = [abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
        M = sum(diff)
        best = 0
        for i in range(len(nums1)):
            if nums1[i] != nums2[i]:
                #이진탐색으로 삽입될 자리의 인덱스를 반환함
                j = bisect_left(nums1, nums2[i])
                if j == len(nums1):
                    best = max(best, diff[i] - abs(nums1[-1] - nums2[i]))
                elif j == 0:
                    best = max(best, diff[i] - abs(nums1[0] - nums2[i]))
                # ex : [1,2,2,3,4,4] 에 2를 넣으면  [1,^2,2,3,4,4] ^자리 인덱스 반환
                # 그니깐 j와, j-1의 값을 검사해야함
                # 예외처리 j = len(nums1), j == 0 
                else: 
                    new = min(abs(nums1[j] - nums2[i]), abs(nums1[j-1] - nums2[i]))
                    best = max(best, diff[i] - new)
        
        return (M - best) % MOD