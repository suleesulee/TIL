def change_money(euro, change_rate) :
    dollar = euro * change_rate / 100
    return dollar



euro = int(input("How many Euros are you exchanging?"))
change_rate = float(input("What is the exchange rate?"))
dollar = round(change_money(euro, change_rate), 2)
print(str(dollar))