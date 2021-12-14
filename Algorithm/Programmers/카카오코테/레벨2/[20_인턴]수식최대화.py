'''
수식 우선순위를 정한다
+-*
+*-
-*+
-+*
*-+
*+-
6가지
수식에따라 먼저 계산하도록 한다..

수식을 먼저 나눈다. 숫자와 수식으로

'''

from itertools import permutations



def solution(expression):
    answer = 0
    priority = [['+', '-', '*'], ['+', '*', '-'], ['-', '+', '*'], ['-', '*', '+'], ['*', '-', '+'], ['*', '+', '-'], ]
    res = []
    
    def operation(n1, n2, op):
        if op == '+':
            return n1 + n2
        elif op == '-':
            return n1 - n2
        else:
            return n1 * n2

    def cal(exp, op):
        tmp = 0
        exp_list = []
        for i in range(len(expression)):
            if expression[i].isdigit():
                #print(expression[i])
                tmp = tmp * 10 + int(expression[i])
            else:
                exp_list.append(tmp)
                exp_list.append(expression[i])
                tmp = 0
        exp_list.append(tmp)

        for p in op:
            stck = []
            while len(exp_list) != 0:
                temp = exp_list.pop(0)
                if temp == p:
                    stck.append(operation(stck.pop(), exp_list.pop(0), p))
                else:
                    stck.append(temp)
            exp_list = stck
        return abs(exp_list[0])
        
    for p in priority:
        res.append(cal(expression, p))
    
    print(res)
    
    return max(res)