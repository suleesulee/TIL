class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = zip(*matrix[::-1])
        
'''
파이썬에서만 사용가능한 특별한 기능
패킹, zip함수를 이용해 돌리는 형식이라는데 
아직까지 확실하게 이해가안됨(210227)
'''
