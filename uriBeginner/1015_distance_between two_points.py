'''
# -*- coding: utf-8 -*-
====1015_distance_between_two_points ====
Read the four values corresponding to the x and y axes of two points in the plane, p1 (x1, y1) and p2 (x2, y2) and
calculate the distance between them, showing four decimal places after the comma, according to the formula:

Distance = ?

Input
The input file contains two lines of data. The first one contains two double values: x1 y1 and the second one also
contains two double values with one digit after the decimal point: x2 y2.

Output
Calculate and print the distance value using the provided formula, with 4 digits after the decimal point.

============TEST==============
====INPUT====
1.0 7.0
5.0 9.0
====OUTPUT====
4.4721
'''
import math
p1 = input()
x1 = float(p1.split(" ")[0])
y1 = float(p1.split(" ")[1])

p2 = input()
x2 = float(p2.split(" ")[0])
y2 = float(p2.split(" ")[1])
distance = math.sqrt(math.pow(x2 - x1,2) + math.pow(y2-y1,2))

print("{:.4f}".format(distance))