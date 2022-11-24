# Lê um valor e mostra com 5% de desconto

p = float(input('Qual o preço do produto?\n R$ '))
print('O produto que custava R$ {}, com desconto de 5% custará R$ {:.2f}.'.format(p, p-(p*5)/100))
