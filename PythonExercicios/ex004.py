#ex004 do professor Gustavo Guanabara
#dissecando uma variável

n = input(print('Digite algo:'))
print('O tipo primitivo do valor digitado é:', type(n))
print('Só tem espaços?', n.isspace()) #função que verifica se o que foi digitado só contém espaços
print('É um número?', n.isnumeric())  #função que verifica se é um número
print('É alfabético?', n.isalpha())   #função verifica se foram digitadas letras ou não
print('É alfanumérico?', n.isalnum()) #função que verifica se o que foi digitado contém letras e números
print('É decimal?', n.isdecimal())    #função que verifica se o valor é um decimal
print('Todas as letras estão em maiúsculo?', n.isupper())           #função que verifica se TODAS as letras estão em maiúsculo
print('Todas as letras estão em minúsculo?', n.islower())           #função que verifica se TODAS as letras estão em minúsculo
print('A varivál está capitalizada? (Somente uma letra maiúscula)', n.istitle())  #função que verifica se apenas a primeira letra está em maiúscula
print('Pode ser impresso?', n.isprintable())


#Métodos em Python utilizam do parenteses ao final, como os listados acima. Exemplo isupper()







