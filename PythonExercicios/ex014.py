#Conversor de temperaturas - Celsius para Fahrenheit

celsius = float(input('Informe a temperatura em ºC: '))
print('A temperatura informada foi de: {:.1f}ºC'.format(celsius))

fah = (celsius * (9/5)) + 32
print('A temperatura de {:.1f}ºC, convertida para Fahrenheit, equivale a {:.1f}ºF'.format(celsius, fah))