'''
# -*- coding: utf-8 -*-
====1035_selection_test01====
Read 4 integer values A, B, C and D. Then if B is greater than C and D is greater than A and if the sum of C and D
is greater than the sum of A and B and if C and D were positives values and if A is even, write the message “Valores
aceitos” (Accepted values). Otherwise, write the message “Valores nao aceitos” (Values not accepted).

Input
Four integer numbers A, B, C and D.

Output
Show the corresponding message after the validation of the values​​.

=========Result_Test=========
====Input====
5 6 7 8
====Output====
Valores nao aceitos

====Input====
2 3 2 6
====Output====
Valores aceitos
'''
numbers = input().split()
A = int(numbers[0])
B = int(numbers[1])
C = int(numbers[2])
D = int(numbers[3])

if((B > C and D > A) and (C+D > A+B) and (C > 0) and (D>0) and (A % 2==0)):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")