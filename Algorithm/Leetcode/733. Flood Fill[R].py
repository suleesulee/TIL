'''
row, col 관련 
python dfs..
dfsfw

'''

#DFS
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        color = image[sr][sc]
        
        if color == newColor:
            return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if c-1 >= 0:
                    dfs(r, c-1)
                if r-1 >= 0:    
                    dfs(r-1, c)
                if r+1 < row:    
                    dfs(r+1, c)
                if c+1 < col:    
                    dfs(r, c+1)
 
        dfs(sr, sc)
        return image

#BFS