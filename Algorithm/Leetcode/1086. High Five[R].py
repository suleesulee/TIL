'''
dict을 통해 mapping 하는형식으로 값을 추가하는 방법에 대해서 꼭 암기하자
mapping[i[0]] = [i[1]] 없으면 리스트로 추가
그위에는 val에 계속 추가
'''


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        mapping = {}
        res = []
        ans = 0
        
        for i in items:
            if i[0] in mapping:
                mapping[i[0]].append(i[1])
            else:
                mapping[i[0]] = [i[1]]
                
        #print(mapping)
        
        
        for i, j in mapping.items():
            j.sort(reverse=True)
            for k in range(5):
                ans += j[k]
            res.append([i, ans//5])
            ans = 0

        res.sort()

        return res
