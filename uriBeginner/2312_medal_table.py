'''
# -*- coding: utf-8 -*-
Somebody messed up the olympic medal table. Your program must put it back in the right order. The order of the countries
in the medal table is given by the number of gold medals. If there's a tie in the number of gold medals, than the country
with more silver medals win. If there's a tie in both gold and silver medals, the country with more bronze medals should
be above. If two or more nations tie in the three kinds of medals, your program must show them in alphabetic order.

Input
Input is the number of participating nations N (0 ≤ N ≤ 500), followed by the list of countries and their gold G (0 ≤ G ≤ 10000),
silver S (0 ≤ S ≤ 10000) and bronze B (0 ≤ B ≤ 10000) medals.

Output
Output should be the list of countries and their gold, silver and bronze medals shown in the specified order.

=========Result_Test=========
====Input====
8
Belgica 2 2 2
Brasil 7 6 6
Franca 10 18 14
Italia 8 12 8
Australia 8 11 10
Colombia 3 2 3
Suica 3 2 2
Tailandia 2 2 2

====Output====
Franca 10 18 14
Italia 8 12 8
Australia 8 11 10
Brasil 7 6 6
Colombia 3 2 3
Suica 3 2 2
Belgica 2 2 2
Tailandia 2 2 2
'''

from operator import itemgetter
N = int(input())
quadro = []
for i in range(N):
  enter= input().split()
  listaPaises = enter[0]
  O = int(enter[1])
  P = int(enter[2])
  B = int(enter[3])
  quadro.append([listaPaises,O,P,B])

quadro = sorted(quadro,key=itemgetter(0))
quadro = sorted(quadro,key=itemgetter(1,2,3),reverse=True)

#print()
for i in range(len(quadro)):
  print(quadro[i][0],quadro[i][1],quadro[i][2],quadro[i][3])