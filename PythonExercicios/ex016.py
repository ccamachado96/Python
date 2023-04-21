#Crie um programa lendo um número real qualquer, e mostre-o como porção inteira


#Forma feita por mim, sozinho

from math import trunc   #Da biblioteca MATH, importe somente TRUNC, que é usado para cortar qualquer valor após a vírgula, no número informado, ficando só a porção inteira do mesmo

num = float(input('Digite um número: '))
print('O núméro digitado foi: {}'.format(num))   #exiba o número digitado na tela

print('O número digitado, somente com sua porção inteira exibida é: {}'.format(trunc(num)))   #exiba o número digitado, truncado com sua parte inteira



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#2ª forma de fazer

import math             #importando a biblioteca completa, mas só usando o trunc nas linhas abaixo:

num = float(input('Digite um número: '))
inteiro = math.trunc(num)                 #usando uma variável para receber o valor truncado de num
print('O núméro digitado foi: {}'.format(num))  

print('O número digitado, somente com sua porção inteira exibida é: {}'.format(inteiro))



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#3ª forma de fazer

import math            

num = float(input('Digite um número: '))           
print('O núméro digitado foi: {}'.format(num))  
print('O número digitado, somente com sua porção inteira exibida é: {}'.format(math.trunc(num)))




#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#4ª forma de fazer

num = float(input('Digite um número: '))
print('O valor digitado foi {}, e sua porção inteira vale: {}'.format(num, int(num)))   #irá mostrar somente a parte inteira do número com a função int(num)

