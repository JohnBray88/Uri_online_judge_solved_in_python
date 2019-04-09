'''
# -*- coding: utf-8 -*-
Read a value of floating point with two decimal places. This represents a monetary value. After this, calculate the
smallest possible number of notes and coins on which the value can be decomposed. The considered notes are of
100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01. Print the message “NOTAS:”
followed by the list of notes and the message “MOEDAS:” followed by the list of coins.

Input
The input file contains a value of floating point N (0 ≤ N ≤ 1000000.00).

Output
Print the minimum quantity of banknotes and coins necessary to change the initial value, as the given example.

=========Result_Test=========
====Input====
576.73
====Output====
NOTAS:
5 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
2 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
3 moeda(s) de R$ 0.01
'''
valor = float(input())
resultado = 'NOTAS:\n'

mod100 = valor % 100
if (mod100 == valor):
    resultado += '%d nota(s) de R$ 100.00\n' % 0
else:
    resultado += '%d nota(s) de R$ 100.00\n' % (valor / 100)

mod50 = mod100 % 50
if (mod50 == mod100):
    resultado += '%d nota(s) de R$ 50.00\n' % 0
else:
    resultado += '%d nota(s) de R$ 50.00\n' % (mod100 / 50)

mod20 = mod50 % 20
if (mod20 == mod50):
    resultado += '%d nota(s) de R$ 20.00\n' % 0
else:
    resultado += '%d nota(s) de R$ 20.00\n' % (mod50 / 20)

mod10 = mod20 % 10
if (mod10 == mod20):
    resultado += '%d nota(s) de R$ 10.00\n' % 0
else:
    resultado += '%d nota(s) de R$ 10.00\n' % (mod20 / 10)

mod5 = mod10 % 5
if (mod5 == mod10):
    resultado += '%d nota(s) de R$ 5.00\n' % 0
else:
    resultado += '%d nota(s) de R$ 5.00\n' % (mod10 / 5)

mod2 = mod5 % 2
if (mod2 == mod5):
    resultado += '%d nota(s) de R$ 2.00\n' % 0
else:
    resultado += '%d nota(s) de R$ 2.00\n' % (mod5 / 2)

resultado += 'MOEDAS:\n'

mod1 = mod2 % 1
if (mod1 == mod2):
    resultado += '%d moeda(s) de R$ 1.00\n' % 0
else:
    resultado += '%d moeda(s) de R$ 1.00\n' % (mod2 / 1)

mod1 = mod1 * 100
mod050 = mod1 % 50
if (mod050 == mod1):
    resultado += '%d moeda(s) de R$ 0.50\n' % 0
else:
    resultado += '%d moeda(s) de R$ 0.50\n' % (mod1 / 50)

mod025 = mod050 % 25
if (mod025 == mod050):
    resultado += '%d moeda(s) de R$ 0.25\n' % 0
else:
    resultado += '%d moeda(s) de R$ 0.25\n' % (mod050 / 25)

mod010 = mod025 % 10
if (mod010 == mod025):
    resultado += '%d moeda(s) de R$ 0.10\n' % 0
else:
    resultado += '%d moeda(s) de R$ 0.10\n' % (mod025 / 10)

mod005 = mod010 % 5
if (mod005 == mod010):
    resultado += '%d moeda(s) de R$ 0.05\n' % 0
else:
    resultado += '%d moeda(s) de R$ 0.05\n' % (mod010 / 5)

mod001 = mod005 % 1
if (mod001 == mod005):
    resultado += '%d moeda(s) de R$ 0.01' % 0
else:
    resultado += '%d moeda(s) de R$ 0.01' % (mod005 / 1)

print(resultado)

'''
#===The Best Solucion
N = float(input())
vN = [100,50,20,10,5,2]
vM = [1,0.50,0.25,0.10,0.05,0.01]
vDN = []
vDM = []
for i in range(len(vN)):
    vDN.append(N/vN[i])
    N = N%vN[i]
for i in range(len(vM)):
    vDM.append(N/vM[i])
    N = N%vM[i]

print("NOTAS:")
for i in range(len(vN)):
    print("{} nota(s) de R$ {:.2f}".format(int(vDN[i]),(vN[i])))
print("MOEDAS:")
for i in range(len(vM)):
    print("{} moeda(s) de R$ {:.2f}".format(int(vDM[i]),(vM[i])))
'''