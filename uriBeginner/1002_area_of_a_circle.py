'''
====1002_Area_of_a_Circle====
# -*- coding: utf-8 -*-
The formula to calculate the area of a circumference is defined as A = π . R2. Considering to this problem that π = 3.14159:

Calculate the area using the formula given in the problem description.

Input
The input contains a value of floating point (double precision), that is the variable R.

Output
Present the message "A=" followed by the value of the variable, as in the example bellow, with four places after the decimal point.
Use all double precision variables. Like all the problems, don't forget to print the end of line after the result, otherwise you will
receive "Presentation Error".

=========Result_Test=========
====Input====
2.00
====Output====
A=12.5664

====Input====
100.64
====Output====
A=31819.3103

====Input====
150.00
====Output====
A=70685.7750

'''
n = 3.14159
A = 0
R = float(input())
A = (n * R**2)
print("A={:.4f}".format(A))

