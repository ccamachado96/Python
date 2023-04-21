#Calculando a raiz de um número usando módulos e biblioteca MATH, exercicio em aula 08

#1º forma de fazer, importando TODA A BIBLIOTECA MATH

import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print('A raiz de {}, vale: {}'.format(num, math.sqrt(num)))



#2ª forma de fazer


import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print('A raiz de {}, vale: {}'.format(num, raiz))



#3ª forma, arredondando o valor da raiz pra cima:

import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print('A raiz de {}, vale: {}'.format(num, math.ceil(raiz)))


#4ª forma arredondando o valor da raiz para baixo:

import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print('A raiz de {}, vale: {}'.format(num, math.floor(raiz)))



#-------------------------------------------------------------


#5ª forma de fazer, IMPORTANDO SOMENTE a função sqrt

from math import sqrt

num = int(input('Digite um número: '))
raiz = sqrt(num)

print('A raiz de {}, vale: {}'.format(num, math.sqrt(num)))