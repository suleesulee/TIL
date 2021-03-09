class Solution:
    def reformatDate(self, date: str) -> str:
        date, month, year = date.split()
        
        months = {
            "Jan" : "01",
            "Feb" : "02",
            "Mar" : "03",
            "Apr" : "04",
            "May" : "05",
            "Jun" : "06",
            "Jul" : "07",
            "Aug" : "08",
            "Sep" : "09",
            "Oct" : "10",
            "Nov" : "11",
            "Dec" : "12"
        }

        d = date[0:2] if len(date) == 4 else "0"+ date[0] # 이런식으로 써낼수있다는걸 기억해야한다.
        m = months[month]
        
        return f'{year}-{m}-{d}' 
        
        # f포맷팅은 py3.x부터지원

# 리스트의 슬라이스 기능을 쓸수있다는거 잊지말아야함 go는 마이너스 움직임 안되는데 파이썬은 됨