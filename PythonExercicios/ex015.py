#Exercicio de aluguel de carros

dias_alugados = int(input('Quantos dias alugados? '))
km = int(input('Quantos KM foram percorridos? '))

custo_dias = dias_alugados * 60
custo_km = km * 0.15
custo_total = custo_dias + custo_km

print('O valor por dia alugado a se pagar é de: R${:.2f}'.format(custo_dias))
print('O valor por KM rodado a se pagar é de: R${:.2f}'.format(custo_km))
print('O valor TOTAL pelo aluguel do carro, a ser pago é de: R${:.2f}'.format(custo_total))

