class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minute = []
        for i in timePoints:
            minute.append(int(i[0:2]) * 60 + int(i[3:]))

        minute.sort()
        ans = 60 * 24 + minute[0] - minute[-1]
        for i in range(1, len(minute)):
            ans = min(ans, minute[i] - minute[i-1])
        
        return ans
        