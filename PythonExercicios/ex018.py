#ex018 - Calculando seno, cosseno e tangente com o IMPORT MATH

#OBS, é necessário passar os valores em RADIANOS, convertendo, com os comandos abaixo (math.radians)

import math

angulo = float(input('Digite o angulo desejado: '))
seno = math.sin(math.radians(angulo))   #Pega o angulo digitado, converte para radianos, e sem seguida, calcula o seno do angulo convertido em radianos
cosseno = math.cos(math.radians(angulo))  #Pega o angulo digitado, converte para radianos, e sem seguida, calcula o cosseno do angulo convertido em radianos
tan = math.tan(math.radians(angulo))     #Pega o angulo digitado, converte para radianos, e sem seguida, calcula a TANGENTE do angulo convertido em radianos

print('O angulo {}, tem o seno de {:.2f}'.format(angulo, seno))
print('O angulo {}, tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O angulo {}, tem o TANGENTE de {:.2f}'.format(angulo, tan))




#------------------------------------------------------------------------------------------------------------------------------------------------------------




#2ª forma, simplificando sem usar toda a biblioteca MATH

from math import radians, tan, cos, sin

angulo = float(input('Digite o angulo desejado: '))
seno = sin(radians(angulo))   #Pega o angulo digitado, converte para radianos, e sem seguida, calcula o seno do angulo convertido em radianos
cosseno = cos(radians(angulo))  #Pega o angulo digitado, converte para radianos, e sem seguida, calcula o cosseno do angulo convertido em radianos
tan = tan(radians(angulo))     #Pega o angulo digitado, converte para radianos, e sem seguida, calcula a TANGENTE do angulo convertido em radianos

print('O angulo {}, tem o seno de {:.2f}'.format(angulo, seno))
print('O angulo {}, tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O angulo {}, tem o TANGENTE de {:.2f}'.format(angulo, tan))