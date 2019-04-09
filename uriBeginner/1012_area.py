'''
# -*- coding: utf-8 -*-
====1012_area====
Make a program that reads three floating point values: A, B and C. Then, calculate and show:
a) the area of the rectangled triangle that has base A and height C.
b) the area of the radius's circle C. (pi = 3.14159)
c) the area of the trapezium which has A and B by base, and C by height.
d) the area of ​​the square that has side B.
e) the area of the rectangle that has sides A and B.

Input
The input file contains three double values with one digit after the decimal point.

Output
The output file must contain 5 lines of data. Each line corresponds to one of the areas described above, always
with a corresponding message (in Portuguese) and one space between the two points and the value. The value calculated
must be presented with 3 digits after the decimal point.

=========Result_Test=========
====Input====
3.0 4.0 5.2
====Output====
TRIANGULO: 7.800
CIRCULO: 84.949
TRAPEZIO: 18.200
QUADRADO: 16.000
RETANGULO: 12.000
'''
values = input().split()
A = float(values[0])
B = float(values[1])
C = float(values[2])
PI = 3.14159
areaTriangle = (1/2)*A*C
areaCircle = PI * pow(C,2)
areaTrapezium = (1/2)*(A+B)*C
areaSquare = B*B
areaRectangle = A*B
print("TRIANGULO: {:.3f}".format(areaTriangle))
print("CIRCULO: {:.3f}".format(areaCircle))
print("TRAPEZIO: {:.3f}".format(areaTrapezium))
print("QUADRADO: {:.3f}".format(areaSquare))
print("RETANGULO: {:.3f}".format(areaRectangle))