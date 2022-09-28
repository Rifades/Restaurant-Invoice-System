#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Rezaul
#
# Created:     25/09/2022
# Copyright:   (c) Rezaul 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
product_database = ['burger', 'pizza', 'fries']
product_price = [190, 390, 90]
total = 0
product_name, product_quantity, unit_price, line_total = [], [], [], []

while True:
    a = input('Please Enter Product Name :').lower()
    while a not in product_database :
        print("Please Enter a Valid Name")
        a = input()
        continue
    product_name.append(a)
    b = input('Please Enter Quantity :')
    while b.isdigit() is False :
        print("Pleae Enter a Valid Numnber")
        b = input ()
        continue
    product_quantity.append(b)
    sequence = int(product_database.index(a))
    total_value = product_price[sequence] * int(b)
    line_total.append(total_value)
    unit_price.append(product_price[sequence])
    decision = input("Do you wish to continue?? ( y / n ) :")
    if decision.casefold() == 'n' :
        break
print(": SL  : Product  : Quantity  : Unit price : Subtotal  :")
print("-"*55)
for e in range(0, len(product_name)):
    print( ":",e+1," "*(2-len(str(e))),":",product_name[e].capitalize()," "*
    (7-len(product_name[e])),":",product_quantity[e]," "*
    (8-len(str(product_quantity[e]))),":",unit_price[e]," "*
    (9-len(str(unit_price[e]))),":",line_total[e]," "*
    (8-len(str(line_total[e]))),":")
print("-"*55)
for i in range(0,len(line_total)):
    total = total + line_total[i]
print(" "*29," Total", " "*4,":",total)
