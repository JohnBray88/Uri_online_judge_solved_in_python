'''
# -*- coding: utf-8 -*-
====1018_bankNotes====
In this problem you have to read an integer value and calculate the smallest possible number of banknotes in
which the value may be decomposed. The possible banknotes are 100, 50, 20, 10, 5, 2 e 1. Print the read value
and the list of banknotes.

Input
The input file contains an integer value N (0 < N < 1000000).

Output
Print the read number and the minimum quantity of each necessary banknotes in Portuguese language, as the given
example. Do not forget to print the end of line after each line, otherwise you will receive “Presentation Error”.

=========Result_Test=========
====Input====
576
====Output====
576
5 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
1 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
0 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00
'''
n = int(input())
n100 = int(n/100)
result = n % 100
n50 = int(result/50)
result = result % 50
n20 = int(result/20)
result = result % 20
n10 = int(result/10)
result = result%10
n5 = int(result/5)
result = result%5
n2 = int(result/2)
result = result%2
n1 = int(result/1)
result = result%1

print("{}".format(n))
print("{} nota(s) de R$ 100,00".format(n100))
print("{} nota(s) de R$ 50,00".format(n50))
print("{} nota(s) de R$ 20,00".format(n20))
print("{} nota(s) de R$ 10,00".format(n10))
print("{} nota(s) de R$ 5,00".format(n5))
print("{} nota(s) de R$ 2,00".format(n2))
print("{} nota(s) de R$ 1,00".format(n1))

'''
#===The best solution
n = int(input())
note = [100,50,20,10,5,2,1]
div = []
for i in range(len(note)):
    div.append(int(n/note[i])) 
    n = int(n%note[i])
    print("{} nota(s) de R$ {}".format(div[i],note[i]))
'''

