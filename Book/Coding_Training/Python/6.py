from datetime import datetime

print("What is your current age?")
age = input()
print("At what age would tou like to retire?")
retire = input()
remain = int(retire) - int(age) 
current_year = datetime.today().year
remain_year = current_year + remain
print("You have "+ str(remain) + " years left until you can retire.\n It's "+ str(current_year) + ", so you can retire in "+ str(remain_year) +".")