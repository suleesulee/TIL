class Solution:
    def isPalindrome(self, s: str) -> bool:
        #s = s.replace(' ','').replace(':','').replace('.','').replace(',','') #이런식으로 구성하면 결국 이상한 문자를 다 찾아서 변환해야해서 안된다
        
        s = ''.join(e for e in s if e.isalnum()).lower() #알파벳과 숫자만 s에 남기고 소문자로 변형
         
        #print(s)
        
        if s == s[::-1]:
            return True
        else:
            return False
        

# 다른 방법은 초기값과 끝값을 설정하고 해당 문자열을 순환하는건데 isalnum을 이용해 하나씩 전진, 후진해가면서 비교하는것이 있다..
