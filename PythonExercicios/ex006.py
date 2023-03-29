n = int(input('Informe um número qualquer: '))

print('O número informado foi: {}'.format(n))

dobro = n*2
triplo = n*3
raiz = n ** (1/2)

print('O dobro de {}, vale {}'.format(n, dobro))
print('O triplo de {}, vale {}'.format(n, triplo))
print('A raiz de {}, vale {:.2f}'.format(n, raiz))


#Comentários

# \n é usado para quebrar a linha
# ** (1/2) - Para calcular a raiz quadrada. Necessário colocar o parenteses devido a ordem de precedência
# :.2f - usado para formatar melhor os números quebrados - 2 significa o número de cada decimais após a vírgula





# 2ª forma:

n = int(input('Informe um número qualquer: '))

print('O número informado foi: {}'.format(n))

print('O dobro de {}, vale {}'.format(n, (n*2)))
print('O triplo de {}, vale {}'.format(n, (n*3)))
print('A raiz de {}, vale {:.2f}'.format(n, (n ** (1/2))))
