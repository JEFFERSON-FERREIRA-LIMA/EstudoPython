# Lê um número e mostra o dobro, triplo e a raíz quadrada

n = int(input("Digite um número: "))

d = n * 2
t = n * 3
r = n ** (1/2)

print('O dobro do valor {} é {},\no triplo é {}\ne a raíz quadrada é {:.2f}.'.format(n, d, t, r))


# ou

# n = int(input("Digite um número: "))

print('O dobro do valor {} é {},\no triplo é {}\ne a raíz quadrada é {:.2f}.'.format(n*2, n*3, n**(1/2)))


# ou

# n = int(input("Digite um número: "))

# print('O dobro do valor {} é {},\no triplo é {}\ne a raíz quadrada é {:.2f}.'.format(n*2, n*3, pow(n,(1/2))))