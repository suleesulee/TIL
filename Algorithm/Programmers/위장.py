from collections import defaultdict
def solution(clothes):
    answer = 1
    d = defaultdict(list)
    
    for i in range(len(clothes)):
        d[clothes[i][1]].append(clothes[i][0])
    
    #print(d)
    
    for v in d.values():
        answer *= len(v) + 1
    
        
    return answer - 1