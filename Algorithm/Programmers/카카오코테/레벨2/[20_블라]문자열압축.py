def solution(s):
    answer = 0
    leng = []
    res = ""
    
    if len(s) == 1:
        return 1
    
    for cut in range(1, len(s)//2 + 1):
        cnt = 1
        temp_str = s[:cut]
        for i in range(cut, len(s), cut):
            if s[i:i+cut] == temp_str:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ""
                res += (str(cnt) + temp_str)
                temp_str = s[i:i+cut]
                cnt = 1
                
        if cnt == 1:
            cnt = ""
        res += str(cnt) + temp_str
        #print(res)
        leng.append(len(res))
        res = ""
        
    return min(leng)