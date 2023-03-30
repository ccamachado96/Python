# Conversor de medidas

medida = float(input('Informe uma medida em metros: '))

cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida / 1000

print('{:.1f} metros, convertido em centrimetros equivale a: {:.1f}cm'.format(medida, cm))

print('{:.1f} metros convertido em milimetros equivale a: {:.1f}mm'.format(medida, mm))

print('{:.2f} metros convertido em decametros equivale a: {:.2f}dam'.format(medida, dam))

print('{:.2f} metros convertido em hectometros equivale a: {:.2f}hm'.format(medida, hm))

print("{:.2f} metros convertido em kilometros equivale a: {:.3f}km".format(medida, km))



#COMENTÁRIOS

# De metro para cm = multiplique por 100
# De metro para milimetro = multiplique por 1000
# De metro para decametro = divida por 10
# De metro para hectometro = divida por 100
# De metro para kilometro = divida por 1000

# {:.x} defina a quantidade de decimais após a vírgula


