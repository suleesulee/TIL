class Solution:
    def calculate(self, s: str) -> int:
        op = list(s)
        stck = []
        
        while idx < len(s):
            if op[idx] == '*':
                cal = str(int(op[idx-1]) * int(op[idx+1]))
                op = op[:idx-1] + op[idx+2:]
                op.insert(idx, cal)
                idx = idx -
            elif op[idx] == '/':
                cal = str(int(op[idx-1]) // int(op[idx+1]))
                op = op[:idx-1] + op[idx+2:]
                op.insert(idx, cal)
                
        