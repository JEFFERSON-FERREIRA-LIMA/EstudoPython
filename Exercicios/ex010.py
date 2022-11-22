# Lê quanto dinheiro tem na carteira e mostra quantos dólares pode gastar, considerae 1 dólar = R$ 5,30

real = float(input('Quanto você tem na carteira? (R$)'))

dolar = real / 5.30

print('Com R${:.2f}, você pode gastar ${:.2f} dólares'.format(real, dolar))
