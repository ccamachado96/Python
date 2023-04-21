#ex017 - Cateto Oposto e Hipotenusa

#1ª forma, matemática de se fazer:

co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Infome o comprimento do cateto adjacente: '))
hip = (co** 2 + ca ** 2)  ** (1/2)                                      #fórmula matemática
print('A hipotenusa vale: {:.2f}'.format(hip))




#---------------------------------------------------------------------------------------------------------------------------------------------------------



#2ª forma, importando a biblioteca MATH, e a função de hypot, que calcula a hipotenusa


import math
co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Infome o comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)                                           #Função da biblioca math
print('A hipotenusa vai medir {:.2f}'.format(hi))




#---------------------------------------------------------------------------------------------------------------------------------------------------------



#3ª forma, mais simples, sem usar TODA a biblioca

from math import hypot
co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Infome o comprimento do cateto adjacente: '))
hi = hypot(co, ca)                                         
print('A hipotenusa vai medir {:.2f}'.format(hi))