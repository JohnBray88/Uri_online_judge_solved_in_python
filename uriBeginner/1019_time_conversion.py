'''
# -*- coding: utf-8 -*-
=====1019_time_conversion=====
Read an integer value, which is the duration in seconds of a certain event in a factory, and inform it expressed in hours:minutes:seconds.

Input
The input file contains an integer N.

Output
Print the read time in the input file (seconds) converted in hours:minutes:seconds like the following example.

=========Result_Test=========
====Input====
556
====Output====
0:9:16
'''

N = int(input())
HH = int(N/3600)
mm = int((N/60) %60)
ss = int(N % 60)
print("{0}:{1}:{2}".format(HH,mm,ss))