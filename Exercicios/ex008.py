# Lê um número e converte em metro´s, centímetros e milímetros

medida = float(input("Digite um número: "))

cm = medida * 100
mm = medida * 1000

print("o valor em centímetros é: {}".format(cm))
print("o valor em milímetros é: {}".format(mm))
