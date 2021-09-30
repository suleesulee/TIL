def solution(p):
    answer = ''

    
    # 올바른 문자열 함수
    def correct(p):
        stck = []
        for c in p:
            if c == '(':
                stck.append(c)
            else:
                if not len(stck):
                    return False
                elif stck[-1] == '(':
                    stck.pop()
        return False if len(stck) else True
        
    
    
    # 올바른 문자열이 아닐때 처리하는 함수
    def change_u(p):
        res = ""
        if not len(p):
            return ""
        u, v = UV(p)
        
        if correct(u):
            res = u + change_u(v)
        else:
            tmp = "("
            tmp += change_u(v)
            tmp += ")"
            u = u[1:-1]
            for c in u:
                if c == '(':
                    tmp += ')'
                else:
                    tmp += '('
                    
            res += tmp
        return res
        
    
    # 균형잡힌문자열로 함수 분리
    def UV(p):
        l, r = 0, 0
        idx = 0
        for i in range(len(p)):
            if p[i] == '(':
                l += 1
            else:
                r += 1

            if r == l:
                u = p[:i+1]
                v = p[i+1:] if i+1 < len(p) else ""
                break
        return u, v  
            

    if correct(p):
        return p
    answer = change_u(p)
    
    
    return answer