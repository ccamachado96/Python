#ex011 Pintando uma parede

#Considerando 1 litro de tinta para cada 2 metros de area

larg = float(input("Informe a largura da parede: "))
alt = float(input('Informe a altura da parede: '))
area = larg * alt

litros = area / 2

print('Sua parede tem a dimensão de: {}x{}, e sua área tem: {}m²'.format(larg, alt, area))

print('Uma parede com {:.2f}m de largura e {:.2f}m de altura usará {:.2f} litros de tinta.'.format(larg, alt, litros))