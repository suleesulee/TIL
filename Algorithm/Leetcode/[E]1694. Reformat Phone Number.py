class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace("-", "").replace(" ", "")
        ans = []
        i = 0
        num_len = len(number)
        
        if num_len < 4:
            return number
        if num_len == 4:
            return number[0:2] +'-' + number[2:]
        
        
        while num_len > 4:
            for _ in range(3):
                ans.append(number[i])
                num_len -= 1
                i+=1
            if num_len > 4:
                ans.append('-')
            
        if num_len < 4:
            ans.append('-')
            ans.append(number[i:])
        else:
            ans.append('-')
            ans.append(number[i:i+2])
            ans.append('-')
            ans.append(number[i+2:])
            
        return ''.join(ans)

#그냥 문자열 잘라내는걸로 풀었는데 코드가 조금 더럽다
#컴팩트하게 짜야한다.