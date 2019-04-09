'''
# -*- coding: utf-8 -*-
====1011_Sphere====
Make a program that calculates and shows the volume of a sphere being provided the value of its radius (R) .
The formula to calculate the volume is: (4/3) * pi * R^3. Consider (assign) for pi the value 3.14159.

Tip: Use (4/3.0) or (4.0/3) in your formula, because some languages (including C++) assume that the division's
result between two integers is another integer. :)

Input
The input contains a value of floating point (double precision).

Output
The output must be a message "VOLUME" like the following example with a space before and after the equal signal.
The value must be presented with 3 digits after the decimal point.

=========Result_Test=========
====Input====
3
====Output====
VOLUME = 113.097
'''
R = float(input())
PI = 3.14159
volSphere = (4/3) * PI * R*R*R
print("VOLUME = {:.3f}".format(volSphere))


'''___Alternative Answer___
import math
R = float(input())
volSphere = (4/3) * math.pi * math.pow(R,3)
print("VOLUME = {:.3f}".format(volSphere))
'''