def main():
    item1 = float(input("Price of item 1: "))
    quantity1 = int(input("Quantitiy of item 1: "))
    item2 = float(input("Price of item 2: "))
    quantity2 = int(input("Quantitiy of item 2: "))
    item3 = float(input("Price of item 3: "))
    quantity3 = int(input("Quantitiy of item 3: "))


    tax_percent = 5.5
    subtotal = item1 * quantity1 + item2 * quantity2 + item3 * quantity3
    tax = round(subtotal * (tax_percent / 100), 2)
    total = subtotal + tax

    print("subtotal: $" + str(subtotal) +"\nTax: $" + str(tax) + "\nTotal: $" + str(total))


main()