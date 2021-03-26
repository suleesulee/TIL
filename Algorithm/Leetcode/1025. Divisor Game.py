#요상한 문제.. 식을 세우다보면 짝수면 무조건 Alice가 이김..


class Solution:
    def divisorGame(self, N: int) -> bool:
        return N%2 == 0