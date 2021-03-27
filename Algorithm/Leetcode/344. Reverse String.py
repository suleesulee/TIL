#파이썬에서는 리스트를 뒤집을수있는 리스트내 함수가 존재한다.
#해당 함수를 쓰면 그냥 풀리는 문제로 문제가 원하는 방법은 이것은 아닐것이다.
#두번째 풀이를 처럼 풀기를 바랬을것이다.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return s.reverse()


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s_len = len(s)
        
        l = 0
        r = s_len - 1
        tmp=[]
        
        while l <= r:
            tmp = s[l]
            s[l] = s[r]
            s[r] = tmp
            l += 1
            r -= 1
        
        return s
        #print(s)