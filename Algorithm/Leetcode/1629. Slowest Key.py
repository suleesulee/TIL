class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxValue = releaseTimes[0]
        diffValue = 0
        key = keysPressed[0]
        
        for i in reversed(range(len(releaseTimes))):
            if i != 0:
                diffValue = releaseTimes[i] - releaseTimes[i-1]
                
                if diffValue > maxValue:
                    maxValue = diffValue
                    key = keysPressed[i]
                elif diffValue == maxValue:
                    key = max(key, keysPressed[i])
                
        return key
        
        
