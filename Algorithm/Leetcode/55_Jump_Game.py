

class Solution:
    def canJump(self, nums: List[int]) -> bool:      
        m = 0
        for idx, n in enumerate(nums):
            if idx > m:
                return False
            m = max(m, idx+n)
        return True

'''
위의 솔루션은 정말 간단하게 풀어냈지만
사실 내가 구현하려했던건
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachableIndex = 0
        for curr in range(len(nums)):
            if curr + nums[curr] >= reachableIndex:
                reachableIndex = curr + nums[curr]
            if curr == reachableIndex:
                break
                
        return reachableIndex >= len(nums) - 1
'''
이런 형식임
처음부터 끝까지 도달가능 범위안에 있는지 확인해서 마지막 인덱스 값에 도달 가능한가를 찾는거였는데
도달가능 인덱스를 리스트에 넣고 풀다가 리스트 범위보다 밖을 찍어내는 경우를 잡아내지 못해서 답을 보게됨
해당 구조가 내가 구현하려 했던 것과 동일한 방식
그냥 한 변수(reachableIndex) 에다가 도달가능 인덱스 최대 값을 계산해 넣고
마지막에 리스트의 길이보와 비교하는것이 더 간단하고 에러를 내지 않는 풀이였음
'''

'''
MEMO
enumerate()는 인덱스와 값을 돌려준다
'''