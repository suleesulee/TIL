#닉네임 변경 -> 나간 후 새로운 닉넴, 기존 채팅방에서 닉넴
#닉변시 -> 기존채팅방의 출력도 변경
#닉 중복 허용
#최종적으로 마지막유저가 보는거 출력
#들어오고 나간거 밖에 안찍힘

# uid = in
# uid = out
# uid = in
# 아이디의 마지막 명을 저장하고 , 아이디= in, out을 기록한 리스트.

def solution(record):
    answer = []
    d = {}
    #입력 각으로 분리
    record_list = []
    record_list_seperate = []
    inout = []
    #for i in range(len(record)):
    record_list += list(record)
    for i in range(len(record_list )):
        record_list_seperate.append(record_list[i].split(' '))
        #print(record_list_seperate)
        

    #print(record_list_seperate)
    #안에서 변경
    #나갔다가 들어가면서 변경
    #인-아웃에 관련된 것 저장
    idx_inout = 0
    for i in range(len(record_list_seperate)):
        if len(record_list_seperate[i]) == 3:
            d[record_list_seperate[i][1]] = record_list_seperate[i][2]
            if record_list_seperate[i][0] != 'Change':
                inout.append([record_list_seperate[i][1], record_list_seperate[i][0]])
                idx_inout+=1
        else:
            inout.append([record_list_seperate[i][1], record_list_seperate[i][0]])
            idx_inout+=1
        
    #print(d)
    #print(inout)
    
    #딕셔너리와 배열에 기초하여 마지막놈이 볼 메시지를만듬
    for i in range(len(inout)):
        name = d[inout[i][0]]
        ans = ""
        if inout[i][1] == 'Enter':
            ans = name + "님이 들어왔습니다."
            #print(ans)
            answer.append(ans)
        else:
            ans = name + "님이 나갔습니다."
            answer.append(ans)
    #print(answer)
    return answer