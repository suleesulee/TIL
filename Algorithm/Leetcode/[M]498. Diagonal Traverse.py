class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        tmp = []
        N = len(mat)    # 4행
        M = len(mat[0]) # 3열
        cnt = 0
        
        # 0, 2, 4
        # 1, 3
        if N == 1 or M == 1:
            for i in range(N):
                for j in range(M):
                    res.append(mat[i][j])
        
        else:
            for d in range(N):
                if d < N :# 행의 숫자
                    c, r = d, 0 
                    while r < M and c > -1:
                        #print(c, r)
                        tmp.append(mat[c][r])
                        c -= 1
                        r += 1
                #print(tmp)
                if d % 2 == 1:
                    tmp = tmp[::-1]
                res += tmp
                tmp.clear()
                cnt += 1            
            for d in range(1, M):
                c, r = N-1, d  #(1, 2)
                #print(c, r)

                while r < M  and c > -1 :
                    #print(c, r)
                    tmp.append(mat[c][r])
                    c -= 1
                    r += 1

                #print(tmp)
                cnt += 1
                if cnt % 2 == 0:
                    tmp = tmp[::-1]
                res += tmp
                tmp.clear()
            
        #print(res)
        return res
'''
Medium
Simulation


시뮬레이션 문제.
접근방법

1. N라인으로 쭉 돌면서 끝까지 간뒤 
2. 1에서 M 라인까지 쭉
3. 짝수차에 reverse




'''