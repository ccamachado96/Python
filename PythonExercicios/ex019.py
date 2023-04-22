#ex019 - Sorteando um item na lista, usando listas e biblioteca RANDOM e método CHOICE

import random    #importando a biblioteca do random

nome1 = input('Informe o nome do primeiro aluno: ')
nome2 = input('Informe o nome do segundo aluno: ')
nome3 = input('Informe o nome do terceiro aluno: ')
nome4 = input('Informe o nome do quarto aluno: ')

lista = [nome1, nome2, nome3, nome4]    #lista em python, par auxiliar a guardar todas as opções

escolhido = random.choice(lista)            #função random.choice, dentro do random, para escolher um valor aleatório dentro da lista declarada acima

print('O aluno escolhido aleatoriamenteo, foi: {}'.format(escolhido))    #imprime o valor escolhido, que ficou armazenado dentro da variável




#----------------------------------------------------------------------------------------------------------------------------------------------------------




#2ª forma de fazer, importando apenas o método CHOICE, de RANDOM


from random import choice

nome1 = input('Informe o nome do primeiro aluno: ')
nome2 = input('Informe o nome do segundo aluno: ')
nome3 = input('Informe o nome do terceiro aluno: ')
nome4 = input('Informe o nome do quarto aluno: ')

lista = [nome1, nome2, nome3, nome4]    

escolhido = choice(lista)           

print('O aluno escolhido aleatoriamenteo, foi: {}'.format(escolhido))