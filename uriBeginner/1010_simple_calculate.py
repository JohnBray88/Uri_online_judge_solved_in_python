'''
# -*- coding: utf-8 -*-
====1010_simple_calculate====
In this problem, the task is to read a code of a product 1, the number of units of product 1, the price for one unit of product 1,
 the code of a product 2, the number of units of product 2 and the price for one unit of product 2. After this, calculate and show
 the amount to be paid.

Input
The input file contains two lines of data. In each line there will be 3 values: two integers and a floating value with 2 digits after
the decimal point.

Output
The output file must be a message like the following example where "Valor a pagar" means Value to Pay. Remember the space after ":" and
after "R$" symbol. The value must be presented with 2 digits after the point.

=========Result_Test=========
====Input====
12 1 5.30
16 2 5.10
====Output====
VALOR A PAGAR: R$ 15.50
'''
prod1 = input().split()
cod1 = int(prod1[0])
qtdeProd1 = int(prod1[1])
valueProd1 = float(prod1[2])
prod2 = input().split()
cod2 = int(prod2[0])
qtdeProd2 = int(prod2[1])
valueProd2 = float(prod2[2])

totalProd1 = qtdeProd1 * valueProd1
totalProd2 = qtdeProd2 * valueProd2
print("VALOR A PAGAR: R$ {:.2f}".format(totalProd1 + totalProd2))