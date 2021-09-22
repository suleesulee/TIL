from collections import deque

def solution(priorities, location):
    answer = 0
    #가장 우선순위 높은게 먼저나오도록 
    dq = deque([(p, i) for i, p in enumerate(priorities)])
    #print(dq)
    while len(dq):
        item = dq.popleft()
        if dq and max(dq)[0] > item[0]:
            dq.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    
    
    
    
    
    return answer