import collections

def solution(participant, completion):
    answer = ''
    p_map = collections.Counter(participant)
    c_map = collections.Counter(completion)
    
    #print(p_map)
    
    ans = p_map-c_map
    l = list(ans.items())
    
    answer = l[0][0]
    
    return answer


