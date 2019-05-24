'''
# -*- coding: utf-8 -*-
Your English teacher loves to bring new stuff to the class, and today it wasn't different. There is a city, according to your
teacher, where the people take really seriously the way they talk to each other. In particular, when two people are talking,
they think a lot in the sentence that they are going to say before they say it, so that they can ensure their sentence will be a
“full sentence”, or maybe an “almost full sentence”.

Considering our 26 letters alphabet, a sentence is “full” if, and only if, it has all the letters of our alphabet in it. In a
similar way, a sentence is “almost full” if, and only if, it is not “full”, but has at least half of the letters of our alphabet
in it. When a sentence is not “full” neither “almost full”, it is “poorly designed”.

Your teacher gave you a really hard task: given several sentences exchanged between several people from the quoted city, say in
which of the given categories each sentence fits in.

Input
The first line contains an integer N, indicating the number of test cases to follow.

Each test case contains one line, containing lowercase letters, white spaces and/or commas. The number of characters of each
line is at least 3 and at most 1000, counting the spaces.

Output
For each test case, print one line containing one of the following sentences: “frase completa”, when the sentence is considered
full; “frase quase completa”, when the sentence is not considered full, but is considered almost full; or “frase mal elaborada”,
when the sentence is not full neither almost full.

=========Result_Test=========
====Input====
2
ola, como voce esta hoje
hoje fui na feira, e comprei banana, melao e abacates
====Output====
frase mal elaborada
frase quase completa
'''

n = int(input())
tupla = (
"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
"y", "z")

for i in range(n):
    new_letter = []
    enter = input()
    for letter in enter:
        if (letter not in new_letter and letter in tupla):
            new_letter.append(letter)

    if (len(new_letter) == 26):
        print("frase completa")
    elif (len(new_letter) >= 13):
        print("frase quase completa")
    else:
        print("frase mal elaborada")

