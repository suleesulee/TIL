# 가장 많이 재생된 거 찾는다.
# 고유번호 먹이면서 찾는다

import collections
def solution(genres, plays):
    answer = []
    d = {}
    for i in range(len(genres)):
        if genres[i] not in d:
            d[genres[i]] = plays[i]
        else:
            d[genres[i]] += plays[i]

    print(d)
    #인덱스와 값을 따로 저장.
    d_list = collections.defaultdict(list)
    for i in range(len(genres)):
        d_list[genres[i]].append([i, plays[i]])

    #print(d_list)
    
    #가장 많이 듣는 분야부터 답에 넣는다
    #두개씩넣는데 하나만있으면 하나만 담는다.
    genre_list = list(d.items())
    genre_list.sort(key = lambda x : -x[1])
    
    #print(genre_list)
    gen_order = []
    for i in range(len(genre_list)):
        gen_order.append(genre_list[i][0])
    
    #print(gen_order)

    
    total_list = list(d_list.items())
    #print(total_list)

    for i in range(len(total_list)):
        total_list[i][1].sort(key = lambda x: -x[1])
    
    #print(total_list)
    
#     #담자
        
    for i in range(len(gen_order)):
        for j in range(len(total_list)):
            if gen_order[i] == total_list[j][0]:
                for k in range(len(total_list[j][1])):
                    #print("!!")
                    if k == 2:
                        break
                    answer.append(total_list[j][1][k][0])
        
    
#     print(total_list[0][1][0][0], total_list[1][0])
#     print(answer)     
    
    
    return answer
