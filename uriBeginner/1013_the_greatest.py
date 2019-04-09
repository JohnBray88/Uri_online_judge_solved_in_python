'''
# -*- coding: utf-8 -*-
====1013_the_greatest====
Make a program that reads 3 integer values and present the greatest one followed by the message "eh o maior".
Use the following formula:
MaiorAB = (a+b+abs(a-b))/2

Input
The input file contains 3 integer values.

Output
Print the greatest of these three values followed by a space and the message “eh o maior”.

=========Result_Test=========
====Input====
7 14 106
====Output====
106 eh o maior
'''
enter = input().split()
A = int(enter[0])
B = int(enter[1])
C = int(enter[2])

MaiorAB = int((A+B+abs(A-B))/2)
MaiorABC = int((MaiorAB+C+abs(MaiorAB-C))/2)

print("{} eh o maior".format(MaiorABC))
