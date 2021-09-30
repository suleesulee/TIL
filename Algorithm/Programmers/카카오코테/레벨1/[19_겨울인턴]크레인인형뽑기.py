def solution(board, moves):
    answer = 0
    pang = []
    
    for i in range(len(moves)):
        loc = moves[i] - 1
        
        for j in range(len(board)):
            if board[j][loc] != 0:
                if pang and pang[-1] == board[j][loc]:
                    answer += 2
                    pang.pop()
                else:
                    pang.append(board[j][loc])
                #print(pang)
                board[j][loc] = 0
                break
                
        
        
    
    return answer