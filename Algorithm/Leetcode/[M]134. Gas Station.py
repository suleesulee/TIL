class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        total, cur = 0, 0
        start = 0
        
        for i in range(n):
            total += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            
            if cur < 0:
                start = i + 1
                cur = 0
            
        return start if total >= 0 else -1

'''
Medium
Greedy


최종적으로 도달할 수 있는지와
현재 위치에서 도달 가능한지 계산함
현재 위치에서 다음위치로 넘어갈 수 없다면 다음 위치에서 다시 시작


'''