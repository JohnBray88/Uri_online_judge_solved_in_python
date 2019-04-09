'''
# -*- coding: utf-8 -*-
Read 3 floating-point numbers. After, print the roots of bhaskara’s formula. If it's impossible to calculate
the roots because a division by zero or a square root of a negative number, presents the message “Impossivel calcular”.

Input
Read 3 floating-point numbers A, B and C.

Output
Print the result with 5 digits after the decimal point or the message if it is impossible to calculate.

=========Result_Test=========
====Input====
10.0 20.1 5.1
====Output====
R1 = -0.29788
R2 = -1.71212
'''
import math
enter = input().split()
A = float(enter[0])
B = float(enter[1])
C = float(enter[2])
delt = math.pow(B,2)-4*A*C
R1 = 0
R2 = 0
if(delt<0.0 or A == 0.0):
    print("Impossivel calcular")
else:
    R1 = (-B+math.sqrt(delt))/(2*A)
    R2 = (-B-math.sqrt(delt))/(2*A)
    print("R1 = {:.5f}".format(R1))
    print("R2 = {:.5f}".format(R2))
