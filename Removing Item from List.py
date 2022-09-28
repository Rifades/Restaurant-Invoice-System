#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Rezaul
#
# Created:     28/09/2022
# Copyright:   (c) Rezaul 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
product_database = ['burger', 'pizza', 'fries']
product_price = [190, 390, 90]

removing_variable = input('Please Enter The Item Name You Want to Remove:').lower()
while removing_variable not in product_database:
    removing_variable = input('Item Already Exist, Please Try Again:').lower()
    continue
to_be_removed = int(product_database.index(removing_variable))
product_database.pop(to_be_removed)
product_price.pop(to_be_removed)
print(product_database, product_price)


