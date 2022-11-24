# Lê a altura e a largura de uma parede em metros, calcula a área e a quantidade de tinta para pintá-la, cada litro pinta 2 metros quadrados

a = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))

print('Sua parede tem uma dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m².\nPara pintá-la, você precisará de {:.2f}l de tinta'.format(a, l, a*l,(a*l)/2))
