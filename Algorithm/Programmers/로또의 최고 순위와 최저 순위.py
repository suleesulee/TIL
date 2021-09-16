def solution(lottos, win_nums):
    answer = []
    
    zero = 0
    correct = 0
    tmp_corr = 0
    for number in lottos:
        if number == 0:
            zero += 1
        if number in win_nums:
            correct += 1
            
    if zero == 6:
        answer.append(1)
        answer.append(6)
    elif zero == 0 and correct == 6:
        answer.append(1)
        answer.append(1)
    
    else:
        tmp_corr = correct + zero
        if tmp_corr == 6:
            answer.append(1)
        elif tmp_corr == 5:
            answer.append(2)
        elif tmp_corr == 4:
            answer.append(3)
        elif tmp_corr == 3:
            answer.append(4)
        elif tmp_corr == 2:
            answer.append(5)
        else:
            answer.append(6)
        
        if correct == 6:
            answer.append(1)
        elif correct == 5:
            answer.append(2)
        elif correct == 4:
            answer.append(3)
        elif correct == 3:
            answer.append(4)
        elif correct == 2:
            answer.append(5)
        else:
            answer.append(6)

    return answer

'''
Lev 1

간단한문제.. 다만 코드가 조금 더럽다.



'''