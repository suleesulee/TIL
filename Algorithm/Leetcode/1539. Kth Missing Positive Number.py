class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        start = 0
        end = len(arr)
        current = 0

        if end == 0:
            return k
        
        while k > 0:
            current += 1
            if arr[start] == current:
                start += 1
                if start == end:
                    return current + k
            
            else:
                k -= 1
                
        return current