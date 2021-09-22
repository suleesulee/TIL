class Solution:
    def originalDigits(self, s: str) -> str:
        str_ans = []
        ans = {}
        
        cnt = collections.Counter(s)
        
        ans['0'] = cnt['z']
        ans['2'] = cnt['w']
        ans['4'] = cnt['u']
        ans['6'] = cnt['x']
        ans['8'] = cnt['g']
        ans['3'] = cnt['h'] - ans['8']
        ans['5'] = cnt['f'] - ans['4']
        ans['7'] = cnt['s'] - ans['6']
        ans['9'] = cnt['i'] - ans['5'] - ans['6'] - ans['8']
        ans['1'] = cnt['n'] - ans['7'] - 2 * ans['9']
        
        #ans_item = list(ans.keys())
        
        print(ans)
        for k, v in ans.items():
            while v > 0:
                str_ans.append(k)
                v-=1
        
        str_ans.sort()
        
        return ''.join(str_ans)

        
        '''
        1
        zero: z
        two: w
        six: x        
        eight: g
        four: u        
        
        2
        three: h
        five: f
        seven: s

        3    
        nine:i 
        
        4
        one:
        '''

'''
Medium
Hash
개인적으로 별로인 문제였다. 
한글자로 구분할 수있는것 빼버리고
제외 글자를 제외하고 하나로 구분할 수 있는것 빼고
이런식으로 답을 구해나가려했다

반복문으로 문자열을 없애가며 답을 구하려했는데 완전 별로인 방식이었고
답을 봤을때 내가 풀려했던 방식을 해시를 통해 조금은 깔끔하게 풀어냈다는 것을 알게되었다.

'''