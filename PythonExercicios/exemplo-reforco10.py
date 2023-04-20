#Exemplo de reforço, calculando desconto no salário


salario_atual = float(input('Informe o salário atual do colaborador: '))
print('O salário atual do colaborador é de: R${:.2f}.'.format(salario_atual))

desconto = salario_atual - (salario_atual * 0.10)

print('O salário de R${:.2f}, do colaborador, com desconto de 10%, passará a ser de: R${:.2f}'.format(salario_atual, desconto))