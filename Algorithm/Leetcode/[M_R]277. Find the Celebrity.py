# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

# n 은 사람수
# knows 는 3 * n 만 사용가능
# 유명인은 나는 아무도 모르는데 다른애들은 나를 알아(중요)
# 반복


class Solution:
    def findCelebrity(self, n: int) -> int:
        self.n = n
        celeb_candi = 0
        for i in range(1, n):
            if knows(celeb_candi, i):
                celeb_candi = i
        if self._is_seleb(celeb_candi):
            return celeb_candi
        return -1
        
    def _is_seleb(self, i):
        for j in range(self.n):
            if i == j:
                continue
            # 이부분이 헷갈린다. i는 j를 알면 안됨 j,i를 알아야함 그래야 True가 나감
            if knows(i, j) or not knows(j,i):
                return False
        return True
    
    
    
'''
Medium
graph

코딩테스트에서 가끔 그래프문제가 나온다 정말 가끔
변별력을 주기위해서 나오는 것 같은데 그래프 이론만 알면 정말 빠르게 풀어낼 수 있는 것이 많다.

셀렙인 친구를 찾기위해 나는 아무도 모른다 하는 녀석을 찾아냄
(누구를 안다 했을 때 타고 타고 넘어가다 나오는 마지막 node)

해당 노드가 진짜 아무도 모르나 탐색

아무도 모르면 답
누군가 알면 -1

'''