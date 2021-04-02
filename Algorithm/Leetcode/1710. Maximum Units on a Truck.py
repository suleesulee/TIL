'''
람다 사용법을 알아야함.. 소팅해서 돌린다는건 알았는데 
소팅을 어떻게 해야하는지 감이안왔다.

'''

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        ans = 0
        
        for box, units in boxTypes:
            if truckSize > box:
                truckSize -= box
                ans += box * units
            else:
                ans += truckSize * units
                return ans
        return ans 
        