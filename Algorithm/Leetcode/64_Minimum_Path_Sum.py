'''
풀이방법은 정확하게 알았고 맞았음
다만 m,n이 주어지는것이 아니라
grid list에서 얻어 내야했는데
grid에서 행과 열을 얻는 방법을 모르겠어서 헤매다 해당 방법을 검색해서 적용
2차원배열이시어... 파이쏜엔 없어 그런거
grid = 행
grid[0] = 열
range(len(grid)), range(len(grid[0]))
외우자!!

그리고 마지막으로 grid[m-1][n-1]에 해당하는 값은 grid[-1][-1]과 같다
'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #print(len(grid), len(grid[0]))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i>0 and j>0 :
                    grid[i][j] = min(grid[i-1][j] + grid[i][j], grid[i][j-1] + grid[i][j])
                elif i > 0: # j == 0
                    grid[i][0] = grid[i][0] + grid[i-1][0]
                elif j > 0: # i == 0 
                    grid[0][j] = grid[0][j] + grid[0][j-1]
        
        return grid[-1][-1]