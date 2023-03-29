#Calculando o Antecessor e Sucessor de um número
#1ª forma

ante = int(input('Informe um número: '))
print('O número digitado foi: {}'.format(ante))

antecessor = ante - 1
sucessor = ante + 1
print('O antecessor de {}, equivale a: {}'.format(ante, antecessor))
print('O sucessor de {}, equivale a: {}'.format(ante, sucessor))




#2ª forma

n = int(input('Informe um número: '))
a = n - 1
s = n + 1
print('O antecessor de {} é {}, e o sucessor é {}'.format(n, a, s))




#3ª forma #sem guardar as informações em variáveis, ou seja, apenas executar o programa uma vez

n = int(input('Informe um número: '))
print('O antecessor de {} é {}, e o sucessor é {}'.format(n, (n-1), (n+1)))

