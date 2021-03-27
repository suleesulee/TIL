'''
DP로 푸는 문제 부르트포스도 가능한데 졸라 복잡..
 _____
| 1| 1| ?는  다른곳이 전부 1일때 2가됨
-------
| 1| ?|
-------
'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row, col = len(matrix), len(matrix[0])

        dp = [[0] * (col+1) for _ in range(row+1)]
        print(dp)
        max_side = 0
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
                    max_side = max(max_side, dp[i+1][j+1])
                    
        return max_side * max_side