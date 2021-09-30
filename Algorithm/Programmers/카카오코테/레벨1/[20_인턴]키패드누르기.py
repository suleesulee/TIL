def solution(numbers, hand):
    answer = ''
    left_thumb = 10
    right_thumb = 12
    
    for i in numbers:
        if i == 1 or i == 4 or i == 7 :
            answer += 'L'
            left_thumb = i
        elif i == 3 or i == 6 or i == 9 :
            answer += 'R'
            right_thumb = i

        else:
            i = 11 if i == 0 else i
                              
            absL = abs(i - left_thumb)
            absR = abs(i - right_thumb)
            
            
            if sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                answer += 'L'
                left_thumb = i                
            elif sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                answer += 'R'
                right_thumb = i
            else:
                if hand == 'right':
                    answer += 'R'
                    right_thumb = i
                else:
                    answer += 'L'
                    left_thumb = i
            
    
    return answer