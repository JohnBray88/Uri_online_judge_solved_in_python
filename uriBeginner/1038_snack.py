'''
# -*- coding: utf-8 -*-
====1038_snack====
Using the following table, write a program that reads a code and the amount of an item. After, print the value to pay.
This is a very simple program with the only intention of practice of selection commands.

            ===table of products??????===

Input
The input file contains two integer numbers X and Y. X is the product code and Y is the quantity of this item according to the above table.

Output
The output must be a message "Total: R$ " followed by the total value to be paid, with 2 digits after the decimal point.

=========Result_Test=========
====Input====
3 2
====Output====
Total: R$ 10.00
'''
enter = input().split()
X = int(enter[0])
Y = int(enter[1])
if(X ==1):
    nameProd="Cachorro Quente"
    priceProd=4.00
elif(X==2):
    nameProd="X-Salada"
    priceProd=4.50
elif(X==3):
    nameProd="X-Bacon"
    priceProd=5.00
elif(X==4):
    nameProd="Torrada simples"
    priceProd=2.00
elif(X==5):
    nameProd="Refrigerante"
    priceProd=1.50

totalPurchase=priceProd*Y
print("Total: R$ {:.2f}".format(totalPurchase))
