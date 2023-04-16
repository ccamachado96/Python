#Calculando desconto MAIS BEM ELABORADO

nome = input('Informe o nome do(a) colaborador(a): ')
print('O nome informado foi: {}.'.format(nome))

salario = float(input('Informe o salário atual do colaborador(a) {}: R$'.format(nome)))
desconto = salario - (salario * 0.10)

print('O salário do(a) colaborador(a){}, de R${:.2f}, sofrendo uma redução de 10%, passa a ser de R${:.2f}'.format(nome, salario, desconto))

