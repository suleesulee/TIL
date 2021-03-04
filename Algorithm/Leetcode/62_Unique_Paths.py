class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        map = [[0 for x in range(n)] for x in range(m)]
        for y in range(n):
            map[0][y] = 1
        for x in range(m):
            map[x][0] = 1
        for x in range(1, m):
            for y in range(1, n):
                map[x][y] = map[x-1][y] + map[x][y-1]
            
            
        #print(map)
        return map[m-1][n-1]