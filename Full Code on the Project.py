#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Rezaul
#
# Created:     29/09/2022
# Copyright:   (c) Rezaul 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tabulate import tabulate
product_database = ['burger', 'pizza', 'fries']
product_price = [190, 290, 100]

while True:
    choice = input('Enter a Choice: \nCreate (C)\nDelete (D)\nView (V)\nInvoice (I)\nExit (E)').upper()
    if choice == 'C':
        checking_variable = input('Please Enter Item Name:').lower()
        while checking_variable.replace(' ', '').isalpha() is False or checking_variable.lower() in product_database:
            checking_variable = input('Please Enter Valid or New Name:')
            continue
        product_database.append(checking_variable)
        new_product_price = input('Please Enter Unit Price')
        while new_product_price.isdigit() is False:
            new_product_price = input('Please Enter Number')
            continue
        product_price.append(int(new_product_price))
        print(product_database, product_price)
        continue
    elif choice == 'D':
        removing_variable = input('Please Enter The Item Name You Want to Remove:').lower()
        while removing_variable not in product_database:
            removing_variable = input('Item Dont Exist, Please Try Again:').lower()
            continue
        to_be_removed = int(product_database.index(removing_variable))
        product_database.pop(to_be_removed)
        product_price.pop(to_be_removed)
        print(product_database, product_price)
        continue
    elif choice == 'V':
        for_pair = []
        final_table = [['Name', 'Unit Price']]
        for i in range(len(product_database)):
            for_pair = [product_database[i], product_price[i]]
            final_table.append(for_pair)
        print(tabulate(final_table, headers='firstrow', tablefmt='fancy_grid', showindex='never'))
        continue
    elif choice == 'I':
        total = 0
        product_name, product_quantity, unit_price, line_total = [], [], [], []
        while True:
            a = input('Please Enter Product Name :').lower()
            while a not in product_database:
                a = input("Please Enter a Valid Name")
                continue
            product_name.append(a)
            b = input('Please Enter Quantity :')
            while b.isdigit() is False:
                b = input("Please Enter a Valid Number")
                continue
            product_quantity.append(b)
            sequence = int(product_database.index(a))
            total_value = product_price[sequence] * int(b)
            line_total.append(total_value)
            unit_price.append(product_price[sequence])
            decision = input("Do you wish to continue?? ( y / n ) :")
            if decision.casefold() == 'n':
                break
        x = []
        y = [['Product Name', 'Product Quantity', 'Unit Price', 'Subtotal']]
        for i in range(len(product_name)):
            x = [product_name[i], product_quantity[i], unit_price[i], line_total[i]]
            y.append(x)
        print(tabulate(y, headers='firstrow', tablefmt='rst'))
        for i in range(0, len(line_total)):
            total = total + line_total[i]
        print(" " * 37, " Total", " " * 10, total)
        continue
    elif choice == 'E':
        print('Thank You')
        break
    else:
        False
