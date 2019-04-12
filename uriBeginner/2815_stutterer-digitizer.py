'''
# -*- coding: utf-8 -*-
====2815_stutterer-digitizer====
Francisco Yote is a different stutterer. Not only does he speak repeating syllables as strangely when he typed a 
text he repeats some syllables, making the reading very annoying. He repeats just syllables that have exactly 2 
letters and never repeats a syllable different than the first syllable of the word. He repeats just one time each 
syllable. For example the word "repeat" can appear as rerepeat, but never as rererepeat.

You have been called as an expert to translate some of Francisco's texts, eliminating the redundancies of text he 
generates.

Input
The input consists of one line with up to 1000 words (each word with up to 15 characters). This line of text should 
be corrected by eliminating redundancies, as presented below.

Output
Your program must generate (from the original text typed by Francisco) a text without the repetitions above mentioned.

=========Result_Test=========
====Input====
Juca comprou fafarinha na memercearia e papagou 4 reais o quilo. A mamae de Juca pediu para ele 
comprar mamais 2 quilos.
====Output====
Juca comprou farinha na mercearia e pagou 4 reais o quilo. A mae de Juca pediu para ele 
comprar mais 2 quilos.
'''

entrada = input().split()
for i in range(len(entrada)):
    if len(entrada[i]) > 3:
        if entrada[i][0:1] == entrada[i][2:3]:
            entrada[i] = entrada[i][2:]
entrada = " ".join(entrada)
print(entrada)

'''
#Outra possibilidade
texto_inicial = input()
texto_final = ' '

lista_texto = texto_inicial.split()

for i in range(len(lista_texto)):
  palavra = lista_texto[i]
  if palavra[0:2] == palavra[2:4]:
    palavra = palavra[2:]
    lista_texto[i] = palavra

# print(lista_texto)
print(texto_final.join(lista_texto))
'''

