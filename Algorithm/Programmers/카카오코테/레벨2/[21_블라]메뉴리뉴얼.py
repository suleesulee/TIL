import itertools
import collections

def solution(orders, course):
    answer = []
    d = {}
    
    for i in course:
        temp = []
        for order in orders:
            combi = itertools.combinations(sorted(order), i)
            temp += combi
        count = collections.Counter(temp)
        print(temp)
        print(count)
        
        if count:
            max_v = max(list(count.values()))
            if max_v >= 2:
                for key, _ in count.items():
                    if count[key] == max_v:
                        answer.append(''.join(key))
        
        #print(d.items())
        #print(max_v)

    return sorted(answer)