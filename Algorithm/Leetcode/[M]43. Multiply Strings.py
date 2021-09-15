class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        int_num1, int_num2 = 0, 0        
        
        for i in num1:
            int_num1 = int_num1 * 10 + (ord(i) - ord('0'))
        
        for i in num2:
            int_num2 = int_num2 * 10 + (ord(i) - ord('0'))
            
        print(int_num1, int_num2)
        int_res = int_num1 * int_num2
        
        str_res = ""
        while int_res:
            str_res += chr(ord('0') + int_res % 10) 
            int_res //= 10
            
        #print(str_res)
        return str_res[::-1]

'''
Medium
Simul

간단하면서도 복잡한 문제
int() 사용금지
ord 테크닉 ord(i) - ord('0') 이면 원래 숫자가 가진 값이 나온다.
다시 변경할때 chr(ord('0')- int_res%10) 하게되면 마지막자리의 문자열로 변경되어 나옴


'''