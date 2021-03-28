'''
부르트포스로 그냥 때려박아 풀려하면 많은 exception 케이스와 마주친다.
결국 제대로 풀지 못해 답을 봤는데
zip함수를 이용하여 모든 strs의 문자를 인덱스별로 묶고
set의 특성인 중복을 포함하지 않음을 이용해서 답인 문자는 리스트에 추가하여 반환하는 알고리즘을 사용했다
*의 사용법이 포인터가 아닌 strs의 모든 리스트들이라는 것을 주의하자

출제 빈도에 비해 문제가 별로 좋지 않다는 평이 많은 문제다.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        zip_list = list(zip(*strs))
        #print(zip_list)
        prefix = ""
        for i in zip_list:
            if len(set(i))==1:
                prefix += i[0]
            else:
                break
        return prefix