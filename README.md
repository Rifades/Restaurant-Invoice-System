# Restaurant Invoice System

## Table of Content
- [Project Overview](#project-overview)
- [Language](#language)
- [Libraries](#libraries)
- [Coding Partitions](#coding-partitions)

### Project Overview

This project aims to create code to run a restaurant invoice system, which allows users to add, view, and remove products and generate a multi-line invoice for printing.

### Language

- Python

### Libraries

- Tabulate

### Coding Partitions

- Adding New Item

```python
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
```

- Removing Item

```python
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
```

- Creation of Invoice

```python
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
```
