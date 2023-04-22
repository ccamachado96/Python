#ex020 - Sorteando uma ordem na lista, usando RANDOM e shuffle

import random

a1 = input('Informe o nome do primeiro aluno: ')
a2 = input('Informe o nome do segundo aluno: ')
a3 = input('Informe o nome do terceiro aluno: ')
a4 = input('Informe o nome do quarto aluno: ')

lista = [a1, a2, a3, a4]   #lista contendo os valores digitados

random.shuffle(lista)     #shuffle é embaralhar, através desse comando dentro da biblioteca RANDOM, a lista com os conteúdos será embaralhada
print('A ordem será: {}'.format(lista))









#2ª forma simplicada - Como só foi usado o suffle, basta importar somente ele


from random import shuffle

a1 = input('Informe o nome do primeiro aluno: ')
a2 = input('Informe o nome do segundo aluno: ')
a3 = input('Informe o nome do terceiro aluno: ')
a4 = input('Informe o nome do quarto aluno: ')

lista = [a1, a2, a3, a4]

shuffle(lista)   
print('A ordem será: {}'.format(lista))
