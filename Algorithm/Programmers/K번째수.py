def solution(array, commands):
    answer = []
    print(len(commands))
    for i in range(len(commands)):
        print(i)
        s = commands[i][0] - 1
        e = commands[i][1]
        target = commands[i][2] - 1
        tmp = array[s:e]
        tmp.sort()
        #print(tmp)
        
        answer.append(tmp[target])
    
    return answer

'''
레벨 1
Sort

그냥 쉬운문제


'''