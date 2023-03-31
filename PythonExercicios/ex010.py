#Conversor de moedas

carteira = float(input('Quanto dinheiro você tem? R$'))

dolar = carteira / 5

print('Com R${:.2f}, você pode comprar U${:.2f} dólar(s).'.format(carteira, dolar))

