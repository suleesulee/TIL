def solution(dartResult):
    answer = 0
    s = []
    star = 0
    sharp = 0
    num = 0
    
    for i in range(len(dartResult)):
        if dartResult[i] == '0' and s and s[-1] == 1 :
            s.pop()
            s.append(10)
        elif dartResult[i].isdigit():
            s.append(int(dartResult[i]))
        else:
            s.append(dartResult[i])

    print(s)
    
    while s:
        v = s.pop()
        if v == '*':
            star += 2
        if v == '#':
            sharp = 1
        
        if v == 'S':
            num = s.pop()
            if star != 0:
                if star > 2 :
                    num = 4 * num
                    star -= 1
                elif star > 0:
                    num = 2 * num
                    star -= 1
            if sharp == 1:
                num = -num
                sharp = 0
        if v == 'D':
            num = s.pop()
            num = num ** 2
            if star != 0:
                if star > 2 :
                    num = 4 * num
                    star -= 1
                elif star > 0:
                    num = 2 * num
                    star -= 1
            if sharp == 1:
                num = -num
                sharp = 0
        if v == 'T':
            num = s.pop()
            num = num ** 3
            if star != 0:
                if star > 2 :
                    num = 4 * num
                    star -= 1
                elif star > 0:
                    num = 2 * num
                    star -= 1
            if sharp == 1:
                num = -num
                sharp = 0
        
        answer += num
        print(answer)
        num = 0
    
    
    return answer