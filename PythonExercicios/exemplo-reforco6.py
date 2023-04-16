#Calculando descontos

salario_atual = float(input('Informe o salário atual do colaborador: R$'))
desconto = salario_atual - (salario_atual * 0.10)

print('O salário atual do colaborador é: R${:.2f}.'.format(salario_atual))
print('O salário de R${:.2f} do colaborador com reajuste, e desconto de 10%, equivale a: R${:.2f}'.format(salario_atual, desconto))


#exercício de fixação