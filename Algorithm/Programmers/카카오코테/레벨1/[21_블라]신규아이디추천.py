import re

def solution(new_id):
    answer = ''
    cnt = 0

    new_id = new_id.lower()
    #print(new_id)

    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    #print(new_id)
    
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    #print(new_id)
    
    
    if len(new_id) > 1:
        if new_id[0] == '.':
            new_id = new_id[1:]
        if new_id[-1] == '.':
            new_id = new_id[0:-1] 
    else:
        if new_id == '.':
            new_id = 'a'

    #print(new_id)
    
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:14]
    
    #print(new_id)

    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]
            
    #print(new_id)
    
    answer = new_id

    return answer