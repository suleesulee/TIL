class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        C = {}
        for i, n in enumerate(nums):
            if n in C:
                C[n].append(i)
            else:
                C[n] = [i]
        M = max([len(i) for i in C.values()])
        
        return min([i[-1]-i[0] for i in C.values() if len(i) == M]) + 1

        
# 리스트컴프리핸션을 잘 활용한 문제.. 모든 인덱스를 기록했다..
# 배워갈점
# 딕셔너리에 밸류를 리스트로 만드는 방법
# 리스트 컴프리핸션을 사용해서 코드를 압축
