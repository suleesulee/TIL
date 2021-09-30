class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        sorted_arr = sorted(arr, key = lambda num : abs(x-num))
        print(sorted_arr)
        
        res = []
        
        for i in range(k):
            res.append(sorted_arr[i])
        
        res.sort()
        
        return res
            