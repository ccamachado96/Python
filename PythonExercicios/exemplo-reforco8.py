#calculando aumento salarial MAIS BEM ELABORADO


n = input('informe o nome do funcionário: ')
print('Nome informado: {}'.format(n))

salario_atual = float(input('Informe o salário atual do funcionário {}: R$'.format(n)))
print('O salário atual do funcionário {} equivale a: R${:.2f}'.format(n,salario_atual))

aumento = salario_atual + (salario_atual * 0.10)
print('O salário de R${:.2f} do funcionário {}, com um aumento de 10%, equivale a R${:.2f}'.format(salario_atual, n, aumento))
