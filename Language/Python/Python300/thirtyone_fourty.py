print("-"*80)

t1 = 'python'
t2 = 'java'
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)

name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13

print("이름: {} 나이{}".format(name1, age1))
print(f'이름 : {name1} 나이 :{age1}\n이름 : {name2} 나이 :{age2}')

상장주식수 = "5,969,782,550"
print(int(상장주식수.replace(',', '')))

분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

data = "    삼성전자    "
print(data.strip())