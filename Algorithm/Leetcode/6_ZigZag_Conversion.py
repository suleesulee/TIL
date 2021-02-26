class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        
        idx = 0
        step = 1
        res = [''] * numRows
        
        for x in s:
            res[idx] += x
            if idx == 0:
                step = 1
            elif idx == numRows-1:
                step = -1
            idx += step
        
        return ''.join(res)