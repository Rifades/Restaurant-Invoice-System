#-------------------------------------------------------------------------------
# Name:        New Item Addition
# Purpose:
#
# Author:      Rezaul
#
# Created:     13/04/2022
# Copyright:   (c) Rezaul 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
product_database = ['burger', 'pizza', 'fries']
product_price = [190, 390, 90]

checking_variable = input('Please Enter Item Name:').lower()
while checking_variable.replace(' ','').isalpha() is False or checking_variable.lower() in product_database:
        checking_variable = input('Please Enter Valid or New Name:')
        continue
product_database.append(checking_variable)
new_product_price = input('Please Enter Unit Price')
while new_product_price.isdigit() is False:
    new_product_price = input('Please Enter Number')
    continue
product_price.append(int(new_product_price))
print(product_database, product_price)
