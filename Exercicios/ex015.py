# Programa que pergunta quantos km um carro alugado percorreu e a quantidade de dias pelos quais ele foi alugado.
# Calcula o preço a pagar, sabendo que o aluguel do carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km = float(input('Quantos km foram percorridos? '))
d = int(input('Por quantos dias ele foi alugado? '))

km_rodado = 0.15 * km
pagar_aluguel = 60 * d

print('O valor a pagar é R$ {:.2f}.'.format(pagar_aluguel + km_rodado))



