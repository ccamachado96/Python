#Exemplo de reforço, calculando aumento no salário

salario_atual = float(input('Informe o salário atual do colaborador: R$'))
print('O salário informado é de: {:.2f}'.format(salario_atual))

aumento = salario_atual + (salario_atual * 0.50)

print('O salário de R${:.2f} do colaborador, com um aumento de 50%, equivale a: R${:.2f}'.format(salario_atual, aumento))

